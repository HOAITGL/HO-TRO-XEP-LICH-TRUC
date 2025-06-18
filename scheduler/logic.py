from models import db
from models.user import User
from models.shift import Shift
from models.schedule import Schedule
from datetime import timedelta
from collections import defaultdict

def generate_schedule(start_date, end_date):
    users = User.query.all()
    shifts = Shift.query.all()
    schedules = []
    user_shift_count = defaultdict(int)
    user_last_days = defaultdict(list)

    Schedule.query.filter(Schedule.work_date >= start_date,
                          Schedule.work_date <= end_date).delete()
    db.session.commit()

    current_date = start_date
    while current_date <= end_date:
        used_users = set()
        for shift in shifts:
            # Ưu tiên bác sĩ đầu tiên
            eligible = [u for u in users if u.role == 'bác sĩ'] + users
            for user in eligible:
                if user.id in used_users:
                    continue
                last_dates = user_last_days[user.id]
                if any(abs((current_date - d).days) < 2 for d in last_dates):
                    continue
                if user_shift_count[user.id] >= 4:  # tối đa 4 ca trong thời gian tạo
                    continue

                schedule = Schedule(user_id=user.id, shift_id=shift.id, work_date=current_date)
                schedules.append(schedule)
                user_shift_count[user.id] += 1
                user_last_days[user.id].append(current_date)
                used_users.add(user.id)
                break
        current_date += timedelta(days=1)

    db.session.bulk_save_objects(schedules)
    db.session.commit()
