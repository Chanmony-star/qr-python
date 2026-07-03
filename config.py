import subprocess


class Config:
    PORT = 5000
    HOST = '0.0.0.0'
    ATTENDANCE_FILE = "attendance.json"
    STUDENTS_FILE = "students.json"
    ADMIN_PASSWORD = "admin123"
    SECRET_KEY = "a2148bd054c172055842dc7d94b651553283f10820f747d6f50e53602df7dd9d"

    @staticmethod
    def get_ip():
        try:
            result = subprocess.run(
                ["hostname", "-I"], capture_output=True, text=True, timeout=2
            )
            ip = result.stdout.strip().split()[0]
            if ip:
                return ip
        except Exception:
            pass
        return "127.0.0.1"
