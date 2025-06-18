import openpyxl
from models.schedule import Schedule

def export_to_excel(file_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Lịch trực"

    ws.append(["Ngày", "Nhân viên", "Ca trực"])

    schedules = Schedule.query.all()
    for s in schedules:
        ws.append([s.work_date, s.user.name, s.shift.name])

    wb.save(file_path)

