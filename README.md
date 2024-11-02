
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

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## Installation and Setup ⚙️

To set up and run this project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/medicine-management-website.git
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
### Project Structure 📂

```plaintext
medicine-management-website/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── app/                   # Django app for patient and medicine management
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   └── views.py
└── users/                 # Django app for user authentication
