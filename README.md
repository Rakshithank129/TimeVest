# TimeVest 🕒💰

**A Django-based web application for managing tasks and tracking investments.**

## Features

👤 User Management
- User Registration & Login
- Secure session-based authentication
 
### 📈 Investment Calculator
- Enter amount & year to calculate future value
- Simple logic for annual investment growth

### ✅ Task Manager
- Task List with Task ID, Name, Priority
- Assign tasks to users with:
  - Edit/Delete/Review controls
  - Assigned By / Assigned To metadata

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default Django DB)

## How to Run the Project Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/timevest.git
   cd timevest

2. **Create a virtual environme**
   python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
3. **Install dependencies**
   pip install -r requirements.txt
4. **Run migrations**
   python manage.py makemigrations
   python manage.py migrate

5.**Run the server**
  python manage.py runserver

6. Open http://127.0.0.1:8000/ in your browser
  
