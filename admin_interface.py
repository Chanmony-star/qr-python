import json
import os
import csv
import io
from datetime import datetime

from config import Config

ATTENDANCE_FILE = Config.ATTENDANCE_FILE
STUDENTS_FILE = Config.STUDENTS_FILE
EXPORT_DIR = "exports"


def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)



def get_today_attendance(attendance=None, today=None):
    """Return only today's records from the flat attendance dict."""
    attendance = attendance if attendance is not None else load_json(ATTENDANCE_FILE)
    today = today or datetime.now().strftime("%Y-%m-%d")
    return {
        sid: record
        for sid, record in attendance.items()
        if record.get("date") == today
    }


def get_stats():
    """Core numbers used by both the CLI and the /admin dashboard."""
    attendance = load_json(ATTENDANCE_FILE)
    students = load_json(STUDENTS_FILE)
    today = datetime.now().strftime("%Y-%m-%d")

    today_records = get_today_attendance(attendance, today)
    total_present = len(today_records)
    total_students = len(students)
    rate = round((total_present / total_students) * 100, 1) if total_students else 0.0

    return {
        "date": today,
        "total_present": total_present,
        "total_students": total_students,
        "rate": rate,
        "absent": max(total_students - total_present, 0),
        "today_records": today_records,
    }



def export_csv_string():
    """Build CSV content in-memory (handy for Flask Response without touching disk)."""
    attendance = load_json(ATTENDANCE_FILE)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Student ID", "Name", "Date", "Time"])
    for sid, record in attendance.items():
        writer.writerow([sid, record.get("name", ""), record.get("date", ""), record.get("time", "")])
    return output.getvalue()


def export_json_string():
    attendance = load_json(ATTENDANCE_FILE)
    return json.dumps(attendance, indent=4)


def export_csv_file(filename=None):
    """Write a CSV file to disk under exports/ -- used by the CLI."""
    os.makedirs(EXPORT_DIR, exist_ok=True)
    filename = filename or f"attendance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    path = os.path.join(EXPORT_DIR, filename)
    with open(path, "w", newline="") as f:
        f.write(export_csv_string())
    return path


def export_json_file(filename=None):
    os.makedirs(EXPORT_DIR, exist_ok=True)
    filename = filename or f"attendance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    path = os.path.join(EXPORT_DIR, filename)
    with open(path, "w") as f:
        f.write(export_json_string())
    return path

def generate_report():
    stats = get_stats()
    lines = []
    lines.append("=" * 44)
    lines.append(f" ATTENDANCE REPORT - {stats['date']}")
    lines.append("=" * 44)
    lines.append(f" Present : {stats['total_present']}")
    lines.append(f" Total   : {stats['total_students']}")
    lines.append(f" Absent  : {stats['absent']}")
    lines.append(f" Rate    : {stats['rate']}%")
    lines.append("-" * 44)

    if not stats["today_records"]:
        lines.append(" No attendance recorded today.")
    else:
        for sid, record in stats["today_records"].items():
            lines.append(f" [OK] {sid:<8} {record.get('name', 'Unknown'):<20} {record.get('time', '')}")

    lines.append("=" * 44)
    return "\n".join(lines)


def print_menu():
    print("\n" + "=" * 40)
    print("   QR ATTENDANCE - ADMIN CONSOLE")
    print("=" * 40)
    print("1. View today's attendance")
    print("2. View statistics")
    print("3. Export CSV")
    print("4. Export JSON")
    print("5. Refresh data")
    print("6. Exit")
    print("=" * 40)


def run_admin_interface():
    print("Starting Admin CLI... (password required)")
    password = input("Enter admin password: ").strip()
    if password != Config.ADMIN_PASSWORD:
        print("Incorrect password. Exiting.")
        return

    print("Login successful.\n")

    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            stats = get_stats()
            if not stats["today_records"]:
                print("\nNo attendance recorded today.")
            else:
                print(f"\nToday's Attendance ({stats['date']}):")
                for sid, record in stats["today_records"].items():
                    print(f"  {sid} - {record.get('name', 'Unknown')} at {record.get('time', '')}")

        elif choice == "2":
            print("\n" + generate_report())

        elif choice == "3":
            path = export_csv_file()
            print(f"\nCSV exported to: {path}")

        elif choice == "4":
            path = export_json_file()
            print(f"\nJSON exported to: {path}")

        elif choice == "5":
            print("\nData refreshed from disk.")

        elif choice == "6":
            print("\nExiting Admin CLI. Goodbye!")
            break

        else:
            print("\nInvalid option, please choose 1-6.")


if __name__ == "__main__":
    run_admin_interface()
