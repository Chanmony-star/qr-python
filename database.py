# database.py
import json
import os
from datetime import datetime
from config import Config

class Database:
    def __init__(self):
        self.attendance_file = Config.ATTENDANCE_FILE
        self.students_file = Config.STUDENTS_FILE
        self.attendance = self.load_attendance()
        self.students = self.load_students()
    
    def load_attendance(self):
        """Load attendance from JSON file"""
        if os.path.exists(self.attendance_file):
            with open(self.attendance_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_attendance(self):
        """Save attendance to JSON file"""
        with open(self.attendance_file, 'w') as f:
            json.dump(self.attendance, f, indent=4)
    
    def load_students(self):
        """Load student database"""
        if os.path.exists(self.students_file):
            with open(self.students_file, 'r') as f:
                return json.load(f)
        return {
            "S001": "Alice Johnson",
            "S002": "Bob Smith",
            "S003": "Charlie Brown"
        }
    
    def mark_attendance(self, student_id, student_name):
        """Mark student as present"""
        today = datetime.now().strftime("%Y-%m-%d")
        now = datetime.now().strftime("%H:%M:%S")
        
        if today not in self.attendance:
            self.attendance[today] = {}
        
        if student_id in self.attendance[today]:
            return False, f"Already marked at {self.attendance[today][student_id]['time']}"
        
        self.attendance[today][student_id] = {
            'name': student_name,
            'time': now,
            'status': 'Present'
        }
        self.save_attendance()
        return True, f"Welcome {student_name}! Logged at {now}"
    
    def get_today_attendance(self):
        """Get today's attendance"""
        today = datetime.now().strftime("%Y-%m-%d")
        return self.attendance.get(today, {})
    
    def get_student(self, student_id):
        """Get student by ID"""
        return self.students.get(student_id)
    
    def get_attendance_report(self):
        """Get full attendance report as text"""
        today = datetime.now().strftime("%Y-%m-%d")
        data = self.get_today_attendance()
        
        if not data:
            return "📊 No attendance recorded today"
        
        output = f"📊 ATTENDANCE REPORT - {today}\n"
        output += "="*40 + "\n\n"
        
        for sid, info in data.items():
            output += f"✅ {sid}: {info['name']} at {info['time']}\n"
        
        output += f"\nTotal: {len(data)} students present"
        return output