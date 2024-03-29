from flask_login import UserMixin
from .. import db


class Leader(db.Model, UserMixin):
    __tablename__ = 'leader'
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(128))
    name = db.Column(db.String(256))
    age = db.Column(db.String(128))
    # city = db.Column(db.String(256))

    def __repr__(self):
        return '%s %s %s %s' % (
            self.id,
            self.group_name,
            self.name,
            self.age)
            # self.city)


    def my_xiashu(self, name):
        from ..models import Qa

        xiashu_info = Qa.query.filter_by(leader=name).all()
        xiashu = []
        for i in xiashu_info:
            xiashu.append(i.name)

        return '%s' % xiashu

