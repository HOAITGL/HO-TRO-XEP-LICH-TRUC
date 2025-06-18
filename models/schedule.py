from models import db
from sqlalchemy.orm import relationship
from datetime import date

class Schedule(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    shift_id = db.Column(db.Integer, db.ForeignKey('shift.id'))
    work_date = db.Column(db.Date)

    user = relationship("User", back_populates="schedules")
    shift = relationship("Shift")
