# routes.py
import io
from datetime import date
from flask import render_template, request, session, redirect, url_for, Response, jsonify
from database import Database
from config import Config

def setup_routes(app):
    app.secret_key = Config.SECRET_KEY
    db = Database()

    @app.route('/admin/login', methods=['GET', 'POST'])
    def admin_login():
        if request.method == 'POST':
            if request.form.get('password') == Config.ADMIN_PASSWORD:
                session['admin_logged_in'] = True
                return redirect(url_for('admin'))
            return render_template('admin_login.html', error="Incorrect password")
        return render_template('admin_login.html')

    def login_required(f):
        from functools import wraps
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not session.get('admin_logged_in'):
                return redirect(url_for('admin_login'))
            return f(*args, **kwargs)
        return wrapper

    @app.route('/')
    def home():
        if session.get('admin_logged_in'):
            return redirect(url_for('admin'))
        return redirect(url_for('admin_login'))

    @app.route('/mark', methods=['GET', 'POST'])
    def mark():
        client_ip = request.remote_addr or ""
        if Config.SCHOOL_SUBNET and not client_ip.startswith(Config.SCHOOL_SUBNET):
            return render_template('error.html', message="Access denied — must use school WiFi")

        if request.method == 'POST':
            student_id = request.form.get('student_id')
            student_name = request.form.get('student_name')

            success, message = db.mark_attendance(student_id, student_name)

            if success:
                return render_template('success.html', message=message)
            else:
                return render_template('error.html', message=message)

        return render_template('mark.html')
    
    @app.route('/mark/<student_id>/<student_name>')
    def mark_student(student_id, student_name):
        client_ip = request.remote_addr or ""
        if Config.SCHOOL_SUBNET and not client_ip.startswith(Config.SCHOOL_SUBNET):
            return render_template('error.html', message="Access denied — must use school WiFi")
        success, message = db.mark_attendance(student_id, student_name)
        if success:
            return render_template('success.html', message=message)
        else:
            return render_template('error.html', message=message)

    @app.route('/students')
    @login_required
    def students():
        return render_template('students_list.html', students=db.students)
    
    @app.route('/admin/logout')
    def admin_logout():
        session.pop('admin_logged_in', None)
        return redirect(url_for('admin_login'))

    @app.route('/admin')
    @login_required
    def admin():
        attendance = db.get_today_attendance()
        total_students = len(db.students)
        present_count = len(attendance)

        return render_template(
            'admin.html',
            attendance=attendance,
            total_students=total_students,
            present_count=present_count,
            total_present=present_count,
            date=date.today().strftime('%Y-%m-%d')
        )
    
    @app.route('/qr')
    @login_required
    def qr():
        return render_template('qr.html')

    @app.route('/admin/qr')
    @login_required
    def admin_qr():
        from time import time
        return render_template('admin_qr.html', timestamp=int(time()))

    @app.route('/qr/class.png')
    def qr_image():
        import qrcode
        mark_url = request.host_url.rstrip('/') + url_for('mark')
        img = qrcode.make(mark_url)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        return Response(buf.getvalue(), mimetype='image/png')
    
    @app.route('/export/csv')
    @login_required
    def export_csv():
        import csv
        import io
        # pyrefly: ignore [missing-import]
        from flask import Response

        attendance = db.get_today_attendance()

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Student ID', 'Name', 'Time', 'Status'])

        for sid, info in attendance.items():
            writer.writerow([sid, info['name'], info['time'], info['status']])

        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=attendance.csv'}
        )

    @app.route('/export/json')
    @login_required
    def export_json():
        from flask import jsonify
        attendance = db.get_today_attendance()
        return jsonify(attendance)

    @app.route('/export/students/csv')
    @login_required
    def export_students_csv():
        import csv, io
        from flask import Response
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Student ID', 'Name'])
        for sid, name in db.students.items():
            writer.writerow([sid, name])
        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=students.csv'}
        )

