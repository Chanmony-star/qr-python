# QR Attendance System

## Project Overview

A pure Python QR code attendance system where students scan QR codes with their phones and log attendance. This version includes HTML templates for a modern, user-friendly web interface.

**Key Features:**
- Pure Python with Flask backend
- HTML templates for beautiful UI
- QR code generation and scanning
- Automatic time and date logging
- JSON file storage (no database needed)
- Mobile-responsive design
- Admin dashboard with statistics
- CSV/JSON export for reports

---

## Team Members & Roles

| Role | Member | Files | Responsibilities |
|------|--------|-------|------------------|
| Team Lead | [Your Name] | app.py, config.py, requirements.txt | Project setup, server integration, final testing |
| Database Developer | Vatana | database.py, data/ | Data storage, JSON operations, file management |
| API Developer | Reaska | routes.py | Web routes, URL handling, request processing |
| QR Code Developer | Jolie | qr_generator.py | QR code generation, image handling |
| Frontend Developer | Lyhour | templates/*.html, static/style.css | HTML templates, CSS styling |
| Admin Interface | Heng | admin_interface.py, templates/admin.html | Admin CLI, dashboard, report generation |
| Tester/Documentation | Vey | test_system.py, README.md | Testing, documentation, quality assurance |

---

## Technologies Used

### Python Libraries
```
Flask==2.3.3      # Web server with HTML templates
qrcode==7.4.2     # QR code generation
Pillow==10.1.0    # Image processing
requests==2.31.0  # HTTP requests (for testing)
```

### Template Engine
- Jinja2 - Flask's default template engine for dynamic HTML

### Python Built-in Modules
```
json      # Data storage
datetime  # Time and date
os        # File operations
csv       # CSV export
```

---

## Project Structure

```
qr_attendance_system/
│
├── app.py                 # Main Flask application (Team Lead)
├── config.py              # Configuration settings (Team Lead)
├── database.py            # Database operations (Vatana)
├── routes.py              # Web routes with HTML rendering (Reaska)
├── qr_generator.py        # QR code generation (Jolie)
├── student_interface.py   # Student CLI (Lyhour)
├── admin_interface.py     # Admin CLI (Heng)
├── test_system.py         # Testing (Vey)
├── requirements.txt       # Python dependencies (Team Lead)
├── README.md              # Project documentation (Vey)
│
├── templates/             # HTML templates (Lyhour)
│   ├── base.html          # Base template (inheritance)
│   ├── index.html         # Home page
│   ├── mark.html          # Student attendance form
│   ├── success.html       # Success page after marking
│   ├── error.html         # Error page
│   ├── admin.html         # Admin dashboard
│   ├── students_list.html # View all students
│   └── qr.html            # QR code display page
│
├── static/                # Static files (Lyhour)
│   ├── style.css          # CSS styling
│   └── images/            # Image assets
│
├── data/                  # Data storage (Vatana)
│   ├── students.json      # Student database
│   └── attendance.json    # Attendance records
│
├── qr_codes/              # Generated QR codes (Jolie)
│   ├── S001_Alice_Johnson.png
│   ├── S002_Bob_Smith.png
│   └── ...
│
└── exports/               # Exported reports (Heng)
    ├── attendance_2026-07-02.csv
    └── attendance_2026-07-02.json
```

---

## How It Works

### Student Flow
```
1. Student opens the system in their browser
   ↓
2. Clicks "Mark Attendance" or scans QR code
   ↓
3. Enters Student ID and Name
   ↓
4. Clicks "Submit" or scans QR code
   ↓
5. System logs attendance with date/time
   ↓
6. Student sees success page with details
```

### Teacher Flow
```
1. Teacher runs python app.py
   ↓
2. Opens the admin dashboard
   ↓
3. Views real-time attendance dashboard
   ↓
4. Sees statistics and student list
   ↓
5. Exports reports as CSV or JSON
```

### QR Code Flow
```
1. Teacher generates QR codes (python qr_generator.py)
   ↓
2. QR codes created in qr_codes/ folder
   ↓
3. Students scan QR codes with phone
   ↓
4. Phone opens link with pre-filled ID/Name
   ↓
5. Attendance automatically marked
```

---

## HTML Pages Overview

| Page | URL | Description |
|------|-----|-------------|
| Home | / | Navigation hub with cards to all features |
| Mark Attendance | /mark | Form for students to enter ID and name |
| Success | /mark (POST) | Confirmation page with student details |
| Error | /error | Error messages and guidance |
| Admin Dashboard | /admin | Statistics, attendance table, export options |
| Students List | /students | All registered students |
| QR Code | /qr | QR code display and instructions |

---

## Installation Guide

### Step 1: Install Python
- Download Python 3.8+ from python.org
- Ensure Python is added to PATH

### Step 2: Clone/Download Project
```
git clone [your-repo-url]
cd qr_attendance_system
```

### Step 3: Create Required Folders
```
mkdir templates static data exports qr_codes
```

### Step 4: Install Dependencies
```
pip install -r requirements.txt
```

Or install individually:
```
pip install flask qrcode Pillow requests
```

### Step 5: Create Student Database
Create `data/students.json`:
```json
{
    "S001": "Alice Johnson",
    "S002": "Bob Smith",
    "S003": "Charlie Brown",
    "S004": "Diana Prince",
    "S005": "Evan Wright"
}
```

### Step 6: Run the Server
```
python app.py
```

### Step 7: Access the System
Open browser and visit the local server address shown in the terminal.

---

## Running the System

### Quick Start Commands

| Command | Purpose |
|---------|---------|
| python app.py | Start the Flask web server |
| python qr_generator.py | Generate QR codes for all students |
| python student_interface.py | Test student interface (CLI) |
| python admin_interface.py | Run admin CLI |
| python test_system.py | Run all tests |

### Access URLs

| URL | Purpose |
|-----|---------|
| / | Home page with navigation |
| /mark | Mark attendance form |
| /admin | Admin dashboard |
| /students | View all students |
| /qr | QR code display |
| /export/csv | Export CSV report |
| /export/json | Export JSON report |

---

## Team Tasks

### Team Lead ([Your Name])
**Files:** app.py, config.py, requirements.txt

**Tasks:**
- Create main Flask application
- Set up configuration
- Install dependencies
- Integrate all team members' work
- Run and test everything
- Coordinate team members

---

### Vatana (Database Developer)
**Files:** database.py, data/

**Tasks:**
- Create JSON storage system
- Implement load/save functions
- Handle attendance marking
- Manage student database
- Create data/ folder structure

---

### Reaska (API Developer)
**Files:** routes.py

**Tasks:**
- Create Flask routes
- Handle URL requests
- Process attendance marking
- Return HTML templates
- Implement CSV/JSON export

**Routes to Implement:**
- / -> Home page
- /mark (GET/POST) -> Attendance form & processing
- /admin -> Dashboard
- /students -> Student list
- /qr -> QR code display
- /export/csv -> CSV download
- /export/json -> JSON download

---

### Jolie (QR Code Developer)
**Files:** qr_generator.py, qr_codes/

**Tasks:**
- Generate student QR codes
- Create QR code folder
- Handle bulk generation
- Test QR scanning
- Generate main QR code for home page

---

### Lyhour (Frontend Developer)
**Files:** templates/*.html, static/style.css, student_interface.py

**Tasks:**
- Create all HTML templates
- Design CSS styling
- Ensure mobile responsiveness
- Create base template for inheritance
- Implement Flask template syntax (Jinja2)
- Create and test student CLI interface

**Templates to Create:**
- base.html - Base template with common layout
- index.html - Home page with navigation cards
- mark.html - Student attendance form
- success.html - Success confirmation
- error.html - Error messages
- admin.html - Admin dashboard
- students_list.html - All students
- qr.html - QR code display

---

### Heng (Admin Interface Developer)
**Files:** admin_interface.py, templates/admin.html

**Tasks:**
- Create admin CLI interface
- Design admin dashboard HTML
- Implement statistics display
- Export functionality
- Report generation

**Admin Features:**
- View today's attendance
- Statistics cards (present, total, rate)
- Attendance table with student details
- Export CSV and JSON buttons
- Refresh data option

---

### Vey (Tester/Documentation)
**Files:** test_system.py, README.md

**Tasks:**
- Write test cases
- Test all components
- Create documentation
- Quality assurance
- Update README with new structure

---

## Testing

### Run All Tests
```
python test_system.py
```

### Test Manually

**1. Test Server:**
Open browser and navigate to the local server address shown when running app.py

**2. Test Marking Attendance:**
- Go to /mark page
- Fill in Student ID and Name
- Click Submit

**3. Test Admin:**
- Go to /admin page
- View attendance dashboard

**4. Test Export:**
- Click "Export CSV" or "Export JSON" buttons

---

## Common Issues

### Issue 1: "Module not found"
```
Solution: Install dependencies
pip install -r requirements.txt
```

### Issue 2: "Address already in use"
```
Solution: Kill process on port 5000
Windows: netstat -ano | findstr :5000
Mac/Linux: lsof -i :5000
```

### Issue 3: "Connection refused"
```
Solution: Make sure server is running
python app.py
```

### Issue 4: QR code not scanning
- Make sure QR code is clear
- Good lighting when scanning
- Use phone camera app

---

## Submission Checklist

### Team Lead ([Your Name])
- [ ] app.py completed and working
- [ ] config.py configured correctly
- [ ] requirements.txt created
- [ ] Server starts successfully
- [ ] All team members' code integrated

### Vatana (Database)
- [ ] database.py completed
- [ ] data/students.json created
- [ ] data/attendance.json created
- [ ] Data saves and loads correctly

### Reaska (API)
- [ ] routes.py completed
- [ ] All routes working
- [ ] Marking attendance works
- [ ] Admin page working
- [ ] Export works

### Jolie (QR)
- [ ] qr_generator.py completed
- [ ] QR codes generated
- [ ] qr_codes/ folder created
- [ ] QR codes scan correctly

### Lyhour (Frontend & Student)
- [ ] All HTML templates created
- [ ] CSS styling complete
- [ ] Templates work with Flask
- [ ] Mobile responsive
- [ ] student_interface.py completed and working

### Heng (Admin)
- [ ] admin_interface.py completed
- [ ] Admin menu works
- [ ] Can view attendance
- [ ] CSV export works

### Vey (Testing)
- [ ] test_system.py completed
- [ ] All tests pass
- [ ] README.md written
- [ ] Documentation complete

---

## Presentation Tips

### What to Show Professor
1. Live Demo
   - Show QR code scanning
   - Student marks attendance
   - Show admin report

2. Code Walkthrough
   - Explain Python-only approach
   - Show HTML templates
   - Demonstrate team work

3. Challenges & Solutions
   - QR generation
   - Data persistence
   - Template rendering

### Key Points to Emphasize
1. 100% Python - No other languages
2. Team Collaboration - Divided tasks
3. Real-World Application - Practical use
4. Simple & Effective - Easy to use
5. Modern UI - HTML templates for better experience

---

## Quick Commands Reference

| Command | Purpose |
|---------|---------|
| python app.py | Start server |
| python qr_generator.py | Generate QR codes |
| python student_interface.py | Test student CLI |
| python admin_interface.py | Run admin CLI |
| python test_system.py | Run all tests |

---

## Need Help?

| Issue | Contact |
|-------|---------|
| Server issues | Team Lead |
| Database issues | Vatana |
| API issues | Reaska |
| QR issues | Jolie |
| Frontend/Student issues | Lyhour |
| Admin issues | Heng |
| Testing issues | Vey |

---
Happy Coding!
