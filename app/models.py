from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager
from .phone.models import Phone
from .leader.models import Leader


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64))

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Qa(db.Model, UserMixin):
    __tablename__ = 'Qa'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    age = db.Column(db.String(128))
    group_name = db.Column(db.String(128))
    phone = db.relationship('Phone', backref='Qa')
    leader = db.Column(db.String(128))

    # @staticmethod
    def phonecount(self, id):
        return '%s' % (Phone.query.filter_by(qa_id=id).count())

    def my_leader(self, group_name):
        leader_info = Leader.query.filter_by(group_name=group_name).first()
        my_leader_name = leader_info.name
        return '%s' % my_leader_name

    def __repr__(self):
        return '<Qa :%s %s %s %s>' % (self.name, self.age, self.id, self.group_name)

