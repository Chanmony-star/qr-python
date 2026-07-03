import json
import os
from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY

ATTENDANCE_FILE = "attendance.json"
STUDENTS_FILE = "students.json"


def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


@app.context_processor
def inject_now():
    now = datetime.now()
    return {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
    }


@app.route("/")
def index():
    return render_template("index.html", server_ip=Config.get_ip())


@app.route("/mark", methods=["GET", "POST"])
def mark():
    if request.method == "POST":
        student_id = request.form.get("student_id", "").strip()
        student_name = request.form.get("student_name", "").strip()
        if not student_id or not student_name:
            return render_template("error.html", error="Student ID and Name are required.")
        students = load_json(STUDENTS_FILE)
        if student_id not in students:
            return render_template("error.html", error=f"Student ID '{student_id}' not found.")
        attendance = load_json(ATTENDANCE_FILE)
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        if student_id in attendance and attendance[student_id].get("date") == date_str:
            return render_template("error.html", error=f"{student_name} ({student_id}) already marked present today.")
        attendance[student_id] = {
            "name": student_name,
            "date": date_str,
            "time": now.strftime("%H:%M:%S"),
        }
        save_json(ATTENDANCE_FILE, attendance)
        return render_template(
            "success.html",
            student_id=student_id,
            student_name=student_name,
        )
    return render_template("mark.html", server_ip=Config.get_ip())


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        password = request.form.get("password", "").strip()
        if password == Config.ADMIN_PASSWORD:
            session["admin_logged_in"] = True
            return redirect(url_for("admin"))
        return render_template("admin_login.html", error="Wrong password.")
    return render_template("admin_login.html", error=None)


@app.route("/admin")
def admin():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))
    attendance = load_json(ATTENDANCE_FILE)
    students = load_json(STUDENTS_FILE)
    today = datetime.now().strftime("%Y-%m-%d")
    total_present = sum(1 for r in attendance.values() if r.get("date") == today)
    return render_template(
        "admin.html",
        attendance=attendance,
        total_present=total_present,
        total_students=len(students),
    )
    
@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("index"))

@app.route("/students")
def students_list():
    students = load_json(STUDENTS_FILE)
    return render_template(
        "students_list.html",
        students=students,
        total_students=len(students),
    )


@app.route("/qr")
def qr():
    return render_template("qr.html", server_ip=Config.get_ip())


if __name__ == "__main__":
    ip = Config.get_ip()
    print(f"\nServer running at http://{ip}:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)

