from sqlalchemy import Column, Integer, String, Time, Float
from models import db

class Shift(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    code = db.Column(String(20), nullable=True)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    duration = Column(Float, nullable=False)

