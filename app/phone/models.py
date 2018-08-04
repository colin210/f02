from flask_login import UserMixin
from .. import  db


class Phone(db.Model,UserMixin):
    __tablename__ = 'phone'
    id = db.Column(db.Integer, primary_key=True)
    machine_os = db.Column(db.String(128))
    machine_year = db.Column(db.String(128))
    machine_pinpai = db.Column(db.String(128))


    def __repr__(self):
        return '<phone :%s %s %s>' % (self.machine_os, self.machine_year, self.machine_pinpai)


