from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import các model ở đây để tránh lỗi vòng lặp
from .user import User
from .shift import Shift
from .schedule import Schedule
