# config.py

class Config:
    PORT = 5000
    HOST = '0.0.0.0'
    ATTENDANCE_FILE = "data/attendance.json"
    STUDENTS_FILE = "data/students.json"

    ADMIN_PASSWORD = "admin123"
    SECRET_KEY = "qr-attendance-secret-key-change-in-production"

    # School WiFi subnet prefix (e.g. "10.190.27."). Leave None for auto-detect.
    SCHOOL_SUBNET = None

    @staticmethod
    def get_ip():
        """Detect LAN IP from hostname -I and auto-populate SCHOOL_SUBNET."""
        import subprocess
        try:
            result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
            ips = result.stdout.strip().split()
            for ip in ips:
                if ip.startswith('10.') or ip.startswith('192.168.'):
                    if Config.SCHOOL_SUBNET is None:
                        Config.SCHOOL_SUBNET = ip[:ip.rfind('.') + 1]
                    return ip
        except:
            pass
        return "127.0.0.1"