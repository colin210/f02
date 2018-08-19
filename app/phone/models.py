from flask_login import UserMixin
from .. import db


class Phone(db.Model, UserMixin):
    __tablename__ = 'phone'
    id = db.Column(db.Integer, primary_key=True)
    machine_os = db.Column(db.String(128))
    machine_year = db.Column(db.String(128))
    machine_pinpai = db.Column(db.String(128))
    machine_owner = db.Column(db.String(256))
    qa_id = db.Column(db.Integer, db.ForeignKey('Qa.id'))

    def __repr__(self):
        return '<phone :%s %s %s %s %s>' % (self.machine_os, self.machine_year, self.machine_pinpai, self.machine_owner,self.qa_id)


