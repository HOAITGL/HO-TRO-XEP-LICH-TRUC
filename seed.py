from models import db
from models.user import User
from models.shift import Shift
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(
        name="Quản trị viên",
        username="admin",
        password="admin",
        role="admin",
        department="Phòng CNTT",
        position="Bác sĩ"
    )

    user1 = User(
        name="Nguyễn Văn A",
        username="nva",
        password="123",
        role="manager",
        department="Khoa Nội",
        position="Điều dưỡng"
    )

    user2 = User(
        name="Trần Thị B",
        username="ttb",
        password="123",
        role="user",
        department="Khoa Ngoại",
        position="Kỹ thuật viên"
    )

    db.session.add_all([admin, user1, user2])
    db.session.commit()
    print("Dữ liệu mẫu đã được khởi tạo.")
