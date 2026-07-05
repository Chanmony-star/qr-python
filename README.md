# QR Attendance System

A **Flask-based** QR code attendance system for classrooms. Students scan a QR code displayed by the teacher, enter their ID and name, and get marked present — all over the school WiFi network. No app installation required.

---

## Problem Statement

Traditional paper-based attendance is slow, easy to cheat, and hard to track over time. Teachers waste 5-10 minutes per class calling names or passing a sign-in sheet. Data is scattered across notebooks and never analyzed.

**This system solves it by:**
- Reducing roll-call to a 3-second QR scan
- Logging date, time, and status automatically
- Restricting access to the school network so students can't mark from home
- Giving the teacher a live dashboard with exportable reports

---

## Features

| Feature | Details |
|---------|---------|
| **QR code display** | Teacher shows one class QR on screen — rotates every 15s |
| **Student scan & mark** | Students scan → enter ID + name → logged instantly |
| **Admin dashboard** | Live count of present/absent/total with percentage |
| **Network lock** | Only devices on school WiFi can mark attendance |
| **CSV / JSON export** | Download attendance data and student lists |
| **Auto-refresh QR** | QR page refreshes every 15 seconds to prevent reuse |
| **Admin login** | Simple password gate for all admin pages |
| **No app install** | Works entirely in the phone browser |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.14 + Flask 3.1 |
| Templates | Jinja2 |
| Storage | JSON files (`data/`) |
| QR generation | `qrcode` + `Pillow` |
| Frontend | Vanilla CSS + responsive layout |
| Network | Flask built-in server, bound to `0.0.0.0` |

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- `pip`
- Phone or second device on the same WiFi

### 1. Clone the repository
```bash
git clone https://github.com/Chanmony-star/qr-python.git
cd qr-python
```

### 2. Install dependencies
```bash
pip install flask qrcode Pillow
```

### 3. Run the server
```bash
python3 app.py
```

You'll see:
```
Server running at http://<your-ip>:5000
```

### 4. Open in browser

| Who | URL | Purpose |
|-----|-----|---------|
| **Teacher** | `http://<your-ip>:5000` | → redirects to admin login |
| **Admin login** | `http://<your-ip>:5000/admin/login` | password: `admin123` |
| **Dashboard** | `/admin` | live attendance view |
| **QR display** | `/admin/qr` | class QR shown to students |
| **Student form** | `/mark` | what students see after scanning |

---

## Team Members

| Role | Member | Files | Responsibilities |
|------|--------|-------|------------------|
| **Team Lead / Backend** | Mony | `app.py`, `config.py` | Flask app setup, server integration, final testing |
| **Database Developer** | Vatana | `database.py`, `students.json`, `attendance.json` | JSON storage, CRUD operations |
| **API / Routes Developer** | Raksa | `routes.py` | URL routing, request handling, export endpoints |
| **QR Code Developer** | Jolie | `qr_generator/qr_code.py` | QR generation, student QR codes |
| **Frontend Developers** | Lyhour & Mony | `templates/*.html`, `static/style.css` | UI design, Jinja2 templates, responsive layout |
| **Admin CLI Developer** | Heng | `admin_interface.py` | Admin dashboard, statistics, CSV/JSON export |
| **Testing & Documentation** | Vey | `test_system.py`, docs | System testing, documentation |

---

## Screenshots

(Add screenshots here after deployment)

| Page | Description |
|------|-------------|
| `screenshots/login.png` | Admin login page |
| `screenshots/dashboard.png` | Admin dashboard with attendance stats |
| `screenshots/qr-display.png` | Class QR code with 15s countdown |
| `screenshots/mark-form.png` | Student attendance form |
| `screenshots/student-scan.png` | What student sees after scanning |

---

## Project Structure

```
qr-python/
├── app.py                      # Flask entry point (Mony)
├── config.py                   # Configuration (port, paths, password)
├── routes.py                   # All Flask routes (Raksa)
├── database.py                 # JSON database layer (Vatana)
├── admin_interface.py          # CLI admin tool (Heng)
├── student_interface.py        # CLI student tool
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── attendance.json         # Attendance records
│   └── students.json           # Student roster
├── static/
│   └── style.css               # Global styles (Lyhour & Mony)
├── templates/
│   ├── base.html               # Base template
│   ├── index.html              # Home page
│   ├── admin.html              # Admin dashboard
│   ├── admin_login.html        # Login page
│   ├── admin_qr.html           # QR display page
│   ├── mark.html               # Student attendance form
│   ├── students_list.html      # Student list
│   ├── success.html            # Success confirmation
│   └── error.html              # Error page
├── qr_generator/
│   ├── qr_code.py              # QR generation script (Jolie)
│   └── qr_codes/               # Generated QR images
└── test_system.py              # Tests (Vey)
```

---

## How It Works (End to End)

```
Student Phone -- scans QR --> QR Code -- POST /mark (ID+Name) --> Flask Server --> JSON File --> Dashboard + Export
```

---

## Future Improvements

- [ ] **Database upgrade** — migrate from JSON to SQLite for concurrent writes
- [ ] **Student registration portal** — let students register their own accounts
- [ ] **Attendance history** — view past days/weeks with charts
- [ ] **Export to PDF** — generate printable class reports
- [ ] **QR watermarking** — add timestamp overlays to prevent screenshot reuse
- [ ] **Multiple classes** — support different sections/subjects per teacher
- [ ] **Parent notifications** — auto-email/SMS when student is absent
- [ ] **Deploy to cloud** — host on a Raspberry Pi or campus server instead of a laptop

---

*Built for school project — ITC, 2026*
