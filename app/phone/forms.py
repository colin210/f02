from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import Required,Length
from .models import Phone
import itertools


class PhoneForm(FlaskForm):
    machine_os = SelectField('OS',validators=[Required()] , choices=[('IOS', 'IOS'),('Android', 'Android')])
    machine_year = StringField('Year')
    # machine_pinpai = StringField('pinpai')
    machine_pinpai = StringField('pinpai', validators=[Required(), Length(1,64)])
    submit = SubmitField('Add')


class PhoneFormEdit(FlaskForm):
    machine_os = SelectField('OS',validators=[Required()] , choices=[('IOS', 'IOS'),('Android', 'Android')])
    machine_year = StringField('Year')
    # machine_pinpai = StringField('pinpai')
    machine_pinpai = StringField('pinpai', validators=[Required(), Length(1,64)])
    submit = SubmitField('Change')


class SelectPhoneForm(FlaskForm):
    machine_pinpai = SelectField('pinpai')
    machine_os = SelectField('OS',validators=[Required()] , choices=[('IOS', 'IOS'),('Android', 'Android')])
    submit = SubmitField('查看')


    def __init__(self,*args,**kwargs):
        super(SelectPhoneForm,self).__init__(*args,**kwargs)
        a =[(v.machine_pinpai,v.machine_pinpai) for v in Phone.query.all()]
        phone_choice =list(set(a))
        self.machine_pinpai.choices = phone_choice
