from sqlalchemy.sql.functions import user
from . import admin
from flask import Flask , render_template , flash , request , session, url_for , redirect
from .utils import admin_only_view
from mod_users.forms import LoginForm , RegisterForm
from mod_users.models import User
from app import db


@admin.route('/')
@admin_only_view
def index():
    all_users = User.query.order_by(User.id.desc()).all()
    users_zero = User.query.filter(User.role == 0).all()
    return render_template('admin/index.html' , users_zero=users_zero , all_users=all_users)


@admin.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash('لطفا تمامی فیلدها را پر کنید' , 'bg-danger')
            return render_template('admin/login.html', form=form)
        user = User.query.filter(User.username.ilike(f"{form.username.data}")).first()

        if not user:
            flash("نام کاربری / رمز ورود  نادرست است", category='bg-danger')
            return render_template('admin/login.html', form=form)

        if not user.check_password(form.password.data):
            flash("نام کاربری / رمز ورود  نادرست است", category='bg-danger')
            return render_template('admin/login.html', form=form)
        
        # if user:
        #     flash("شما از قبل وارد شده اید", category='bg-danger)
        #     return(redirect(url_for('index')))
        
        session['user_id'] = user.id
        session['showname'] = user.showname
        session['username'] = user.username
        session['role'] = user.role
        

        if user.role == 1:
            flash("ورود با موفقیت انجام شد", category='bg-success')
            return redirect(url_for('admin.index'))

        # return redirect(url_for('index'))
    
    if session.get('role') == 1:
        flash("ورود با موفقیت انجام شد", category='bg-success')
        return redirect(url_for('admin.index'))

    

    return render_template('admin/login.html' , form = form)


@admin.route('/register', methods=['GET','POST'])
@admin_only_view
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        # if not form.validate_on_submit():
        #     flash('لطفا تمامی فیلدها را پر کنید' , 'bg-danger')
        #     return render_template('admin/index.html', form=form)
        if not form.password.data == form.confirm_password.data:
            flash('رمز عبور وتکرار رمز عبور مطابقت ندارد' , 'bg-danger')
            return redirect(url_for('admin.index'))
        
        # phone_number_int = len(f"{form.phone_number.data}")
        # if not phone_number_int >= 10:
        #     flash('شماره تلفن صحیح نیست!' , 'bg-danger')
        #     return render_template('admin/index.html', form=form)
        old_username = User.query.filter(User.username.ilike(form.username.data)).first()
        if old_username:
            flash('نام کاربری تکراری میباشد' , 'bg-danger')
            return redirect(url_for('admin.index'))


        

        new_user = User()
        new_user.username = form.username.data
        new_user.showname = form.showname.data
        new_user.set_password(form.password.data)
        new_user.role = form.role.data
        db.session.add(new_user)
        db.session.commit()
        print(form.username.data)
        flash('کاربر با موفقیت افزوده شد' , 'bg-success')
        return redirect(url_for('admin.index'))
        # except IntegrityError:
        #     db.session.rollback()
        #     flash('Email is in use.' , 'bg-danger')
    return render_template('admin/index.html', form=form)

