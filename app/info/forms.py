from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField
from wtforms.validators import Required,Length
from wtforms import ValidationError
from wtforms.fields import core




class QaForm(FlaskForm):
    name = StringField('Name', validators=[Required(), Length(1,64)])
    age = StringField('Age', validators=[Required(),Length(1,64)])

    submit = SubmitField('Add')

class QaFormEdit(FlaskForm):
    name = StringField('Name', validators=[Required(), Length(1,64)])
    age = StringField('Age', validators=[Required(),Length(1,64)])

    submit = SubmitField('Change')

