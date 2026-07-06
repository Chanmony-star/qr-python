# config.py

class Config:
    PORT = 5000
    HOST = '0.0.0.0'
    ATTENDANCE_FILE = "data/attendance.json"
    STUDENTS_FILE = "data/students.json"

    ADMIN_PASSWORD = "admin123"
    SECRET_KEY = "qr-attendance-secret-key-change-in-production"

    SCHOOL_PREFIX = None

    @staticmethod
    def get_ip():
        import subprocess
        try:
            result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
            ips = result.stdout.strip().split()
            for ip in ips:
                if ip.startswith('10.') or ip.startswith('192.168.'):
                    Config.SCHOOL_PREFIX = ip[:ip.rfind('.') + 1]
                    return ip
        except:
            pass
        Config.SCHOOL_PREFIX = "10."
        return "127.0.0.1"