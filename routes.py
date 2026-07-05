# routes.py
from flask import render_template, request
from database import Database

def setup_routes(app):
    db = Database()

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/mark', methods=['GET', 'POST'])
    def mark():
        if request.method == 'POST':
            student_id = request.form.get('student_id')
            student_name = request.form.get('student_name')

            success, message = db.mark_attendance(student_id, student_name)

            if success:
                return render_template('success.html', message=message)
            else:
                return render_template('error.html', message=message)

        return render_template('mark.html')
    
    @app.route('/students')
    def students():
        return render_template('students_list.html', students=db.students)
    
    @app.route('/admin')
    def admin():
        attendance = db.get_today_attendance()
        total_students = len(db.students)
        present_count = len(attendance)

        return render_template(
            'admin.html',
            attendance=attendance,
            total_students=total_students,
            present_count=present_count
        )
    
    @app.route('/qr')
    def qr():
        return render_template('qr.html')
    
    @app.route('/export/csv')
    def export_csv():
        import csv
        import io
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
    def export_json():
        from flask import jsonify
        attendance = db.get_today_attendance()
        return jsonify(attendance)
    
