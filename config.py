# config.py

class Config:
    PORT = 5000
    HOST = '0.0.0.0'
    ATTENDANCE_FILE = "data/attendance.json"
    STUDENTS_FILE = "data/students.json"

    ADMIN_PASSWORD = "admin123"
    SECRET_KEY = "qr-attendance-secret-key-change-in-production"

    # ─── Network restriction ───────────────────────────────────────────────
    # Set this to your school WiFi subnet prefix (with trailing dot).
    # Example: "10.5.6."  or  "192.168.1."
    #
    # Only devices whose IP starts with this prefix can mark attendance.
    # Leave None to DISABLE network restriction (allow from any network).
    #
    # >>> How to find your subnet <<<
    #   1. On your laptop (connected to school WiFi), run:  hostname -I
    #   2. Take the first 3 octets + dot, e.g.  192.168.1.
    #   3. Put it below
    #
    # │ NOTE: If you leave SCHOOL_SUBNET = None, the server will try to    │
    # │ detect it automatically from your WiFi IP at startup.              │
    # │ Set it manually to override the auto-detect.                       │
    SCHOOL_SUBNET = None   # ← override with your subnet, e.g. "192.168.1."

    @staticmethod
    def get_ip():
        """Get this server's LAN IP and auto-set SCHOOL_SUBNET if not configured."""
        import subprocess
        try:
            result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
            ips = result.stdout.strip().split()
            for ip in ips:
                if ip.startswith('10.') or ip.startswith('192.168.'):
                    # Auto-populate subnet from the first matching IP
                    if Config.SCHOOL_SUBNET is None:
                        Config.SCHOOL_SUBNET = ip[:ip.rfind('.') + 1]
                    return ip
        except:
            pass
        return "127.0.0.1"