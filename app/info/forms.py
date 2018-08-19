from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,SelectField
from wtforms.validators import Required,Length
from wtforms import ValidationError
from wtforms.fields import core
from ..config_info import GROUP_INFO


class QaForm(FlaskForm):
    name = StringField('Name', validators=[Required(), Length(1, 64)])
    age = StringField('Age', validators=[Required(),Length(1, 64)])
    group_name = SelectField('Group', choices=GROUP_INFO)

    submit = SubmitField('Add')



# class QaFormEdit(FlaskForm):
#     name = StringField('Name', validators=[Required(), Length(1,64)])
#     age = StringField('Age', validators=[Required(),Length(1,64)])
#
#     submit = SubmitField('Change')
#
