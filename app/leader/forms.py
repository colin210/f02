from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField, BooleanField
from wtforms.validators import Required, Length
# from .models import Leader
from ..config_info import GROUP_INFO


class LeaderForm(FlaskForm):
    group_name = SelectField('Group', choices=GROUP_INFO)
    age = StringField('age')
    name = StringField('name', validators=[Required()])
    submit = SubmitField('Add')

    # def __init__(self, *args, **kwargs):
    #     from ..config_info import GROUP_INFO
    #
    #     super(LeaderForm, self).__init__(*args, **kwargs)
    #
    #     self.group_name.choices = GROUP_INFO
