# config.py

class Config:
    PORT = 5000
    HOST = '0.0.0.0'
    ATTENDANCE_FILE = "data/attendance.json"
    STUDENTS_FILE = "data/students.json"

    ADMIN_PASSWORD = "admin123"
    SECRET_KEY = "qr-attendance-secret-key-change-in-production"

    # Set this to your school WiFi subnet prefix (with trailing dot)
    SCHOOL_SUBNET = None

    @staticmethod
    def get_ip():
        """Get this server's LAN IP (for the startup banner)."""
        import subprocess
        try:
            result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
            ips = result.stdout.strip().split()
            for ip in ips:
                if ip.startswith('10.') or ip.startswith('192.168.'):
                    return ip
        except:
            pass
        return "127.0.0.1"