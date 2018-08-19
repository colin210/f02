from flask import Blueprint

leader = Blueprint('leader', __name__)


from . import views


