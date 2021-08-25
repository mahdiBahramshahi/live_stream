from flask import render_template , request , flash , session ,redirect,url_for
from mod_users.forms import LoginForm
from mod_users.models import User
from . import users
from app import app
import pyscreenshot
import flask
from io import BytesIO

# @users.route('/')
# def index():
#     return render_template('index.html')

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash('لطفا تمامی فیلدها را پر کنید' , 'bg-danger')
            return render_template('index.html', form=form)
        user = User.query.filter(User.username.ilike(f"{form.username.data}")).first()

        if not user:
            flash("نام کاربری / رمز ورود  نادرست است", category='bg-danger')
            return render_template('index.html', form=form)

        if not user.check_password(form.password.data):
            flash("نام کاربری / رمز ورود  نادرست است", category='bg-danger')
            return render_template('index.html', form=form)
        
        # if user:
        #     flash("شما از قبل وارد شده اید", category='bg-danger)
        #     return(redirect(url_for('index')))
        
        session['user_id'] = user.id
        session['showname'] = user.showname
        session['username'] = user.username
        session['role'] = user.role
        

        # if user.role == 1:
        #     # flash("ورود با موفقیت انجام شد", category='bg-success')
        #     return redirect(url_for('admin.webinar'))

        # return redirect(url_for('index'))
    
    # if session.get('role') == 1:
    #     # flash("ورود با موفقیت انجام شد", category='bg-success')
    #     return redirect(url_for('admin.webinar'))
    
    if session.get('username') is not None:
        # flash("ورود با موفقیت انجام شد", category='bg-success')
        return redirect(url_for('users.webinar'))
    

    return render_template('index.html', form=form)



@users.route('/webinar/',methods=['GET','POST'])
def webinar():
    if not session.get('username'):
        flash('شما حساب کاربری ندارید.', category='bg-danger')
        return redirect(url_for('index')) 
    return render_template('webinar.html')






