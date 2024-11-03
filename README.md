
# Medicine Management Website 🏥💊

A comprehensive web application designed to help users manage patient information and track medications. Users can log in, add multiple patients, and manage their medication details seamlessly. Built with **Django**, **Python**, **HTML**, **CSS**, and **JavaScript**.

## Features ✨

- 🔒 **User Authentication**: Secure login system for user accounts.
- 🧑‍⚕️ **Patient Management**: Users can add multiple patients and store their details.
- 💊 **Medicine Management**:
  - Add, edit, update, and delete medicine records for each patient.
  - Track details, including medicine names, dosages, and schedules.
- 📱 **Responsive Design**: User-friendly interface, compatible with various devices.

## Technologies Used 🛠️

- **Django** and **Django REST Framework** for backend and API development
- **JWT Authentication** (or Django’s built-in authentication) for user management
  
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## 🚀 Getting Started

### Prerequisites
- Python 3
- Django and Django REST Framework installed


### Installation and Setup ⚙️

To set up and run this project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Neh2005/Medicine-management-django.git
   cd medicine-management-website
   
2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run Database Migrations**
   ```bash
   python manage.py migrate
5. **Start the Development Server**
   ```bash
   python manage.py runserver
6. **Access the Website**
   
   Open your browser and go to http://127.0.0.1:8000/.

### Database Management

This project uses **phpMyAdmin** for database management with **MySQL**. Make sure to configure the database connection in your Django settings.

---

### API Endpoints

- `/api/auth/`: Authentication endpoints for registration and login
- `/api/medicines/`: Endpoints to add, edit, delete, and update medicine details
- `/api/patients/`: Endpoints to manage patient records

## 📚 Key Features

- **User Authentication**: Only registered users can access the system.
- **Full CRUD Operations**: Perform all CRUD operations on medicines and patient records.
- **Secure Data Access**: User data is protected, and each user can only access their own records.

### Usage 👥

- **User Login**: Register and log in to access your account.
- **Patient Management**: Add patients and store their details.
- **Medicine Management**:
  - Add new medications with dosage and schedule information.
  - Update or delete records as needed.


