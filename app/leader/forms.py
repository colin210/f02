from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField, BooleanField
from wtforms.validators import Required, Length
# from .models import Leader


class LeaderForm(FlaskForm):
    group_name = StringField('Group')
    age = StringField('age')
    name = StringField('name', validators=[Required()])
    submit = SubmitField('Add')





