from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField, BooleanField
from wtforms.validators import Required, Length
from .models import Phone


class PhoneForm(FlaskForm):
    machine_os = SelectField('OS',validators=[Required()] , choices=[('IOS', 'IOS'),('Android', 'Android')])
    machine_year = StringField('Year')
    machine_owner = SelectField('Owner')
    machine_pinpai = StringField('pinpai', validators=[Required(), Length(1, 64)])
    submit = SubmitField('Add')

    def __init__(self, *args, **kwargs):
        from ..models import Qa

        super(PhoneForm, self).__init__(*args, **kwargs)
        a = [(v.name, v.name) for v in Qa.query.all()]
        qa_choice = list(set(a))
        self.machine_owner.choices = qa_choice


class PhoneFormEdit(FlaskForm):
    machine_os = SelectField('OS',validators=[Required()] , choices=[('IOS', 'IOS'),('Android', 'Android')])
    machine_year = StringField('Year')
    machine_owner = SelectField('Owner')
    machine_pinpai = StringField('pinpai', validators=[Required(), Length(1, 64)])
    submit = SubmitField('Change')

    def __init__(self,*args,**kwargs):
        from ..models import Qa

        super(PhoneFormEdit, self).__init__(*args, **kwargs)
        a = [(v.name, v.name) for v in Qa.query.all()]
        qa_choice = list(set(a))
        self.machine_owner.choices = qa_choice


class SelectPhoneForm(FlaskForm):
    machine_pinpai = SelectField('pinpai')
    b1 = BooleanField('use', default='checked')
    machine_owner = SelectField('Owner')
    b2 = BooleanField('use', default='checked')
    machine_os = SelectField('OS', validators=[Required()], choices=[('IOS', 'IOS'), ('Android', 'Android')])
    b3 = BooleanField('use', default='checked')
    submit = SubmitField('查看')

    def __init__(self,*args,**kwargs):
        super(SelectPhoneForm,self).__init__(*args,**kwargs)
        a = [(v.machine_pinpai,v.machine_pinpai) for v in Phone.query.all()]
        b = [(v.machine_owner,v.machine_owner) for v in Phone.query.all()]
        phone_choice = list(set(a))
        owner_choice = list(set(b))
        self.machine_pinpai.choices = phone_choice
        self.machine_owner.choices = owner_choice


