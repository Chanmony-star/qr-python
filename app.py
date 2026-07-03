# app.py
from flask import Flask
from routes import setup_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
setup_routes(app)

if __name__ == '__main__':
    ip = Config.get_ip()
    print(f"\n Server running at http://{ip}:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)