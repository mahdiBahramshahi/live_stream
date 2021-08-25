from flask_wtf import FlaskForm
from wtforms import PasswordField , StringField , SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = PasswordField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])


class RegisterForm(FlaskForm):
    showname= StringField(validators=[DataRequired()])
    username= StringField(validators=[DataRequired()])
    password= PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired()])
    role = SelectField(u'role', choices=[('-', '-'),('', '')])