from flask import Blueprint

phone = Blueprint('phone', __name__)


from . import views


