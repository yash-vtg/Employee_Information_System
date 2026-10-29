# 🏢 Employee Information System

A full-stack web application built with **Python** and **Django** designed to efficiently store, manage, and update employee records. The application features a mobile-first, responsive user interface built with **Bootstrap** and leverages the built-in **Django Administration Panel** for complete backend data control.

---

## ✨ Key Features

* **Store Employee Records:** Easily add and store comprehensive employee details in a centralized database.
* **Edit & Update Details:** Seamlessly modify existing employee information as roles, contact details, or departments change.
* **Responsive Interface:** Built with Bootstrap to ensure smooth navigation and usability across desktops, tablets, and mobile devices.
* **Django Admin Integration:** Administrators have full CRUD (Create, Read, Update, Delete) access to manage all employee records directly from the secure Django Administration panel.
* **Lightweight & Fast Database:** Powered by SQLite for zero-configuration, reliable local data storage.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
* **Backend:** Python, Django
* **Database:** SQLite3

---

## 🚀 Getting Started (Installation & Setup)

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
git clone (https://github.com/yash-vtg/Employee_Information_System.git)
cd employee_information_system

### 2. Create and Activate a Virtual Environment
* **Windows:**
  python -m venv venv
  venv\Scripts\activate
* **macOS / Linux:**
  python3 -m venv venv
  source venv/bin/activate

### 3. Install Dependencies
pip install django

*(Or if you have a requirements file: `pip install -r requirements.txt`)*

### 4. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create an Admin Superuser
To access the Django Administration panel and manage employee data, create a superuser account:
python manage.py createsuperuser

*(Follow the prompts to set your username, email, and password.)*

### 6. Run the Development Server
python manage.py runserver

---

## 💻 Usage

1. **Main Application:** Open your browser and go to `http://127.0.0.1:8000/` to view, add, and edit employee records through the responsive web interface.
2. **Admin Panel:** Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials to view, edit, filter, or delete complete employee information directly from the backend.

---

## 📂 Project Structure

employee-information-system/
├── manage.py
├── db.sqlite3
├── project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── employee_app/
    ├── migrations/
    ├── static/
    │   ├── css/
    │   └── js/
    ├── templates/
    ├── admin.py
    ├── models.py
    ├── urls.py
    └── views.py

---

## 📄 License

This project is open-source and available for educational and personal use.
