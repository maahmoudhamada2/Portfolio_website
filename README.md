# Portfolio_webstie

## Introduction

This is a **Portfolio Website** designed to showcase the developer's projects and blogs. The website is built using **Flask** for the back-end, **SQLAlchemy** for database management, and **HTML/CSS/JavaScript** for the front-end. It also features an **Admin Panel** for managing blogs and projects through a command-line interface.

**Features:**
- Showcase projects with descriptions, technologies used, and links to GitHub.
- Display blogs on various topics written by the developer.
- Admin panel for managing content (projects and blogs).
- Contact form to get in touch with the developer.

### Live Site:
[Live Project Link](#)

### Project Blog:
[Project Blog Article](#)

**Author:**  
[Your LinkedIn Profile](#)

---

## Installation

### Prerequisites
- **Python 3.x**
- **MySQL**
- **Flask** and required dependencies (install via `requirements.txt`)

### Steps to Install

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/yourrepository.git

2. **Navigate to the project directory:**
    ```bash
    cd yourrepository
3. Set up a virtual environment (optional):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
4. Install the project dependencies:

   ```bash
      pip install -r requirements.txt
5.Set up the MySQL database:
  - **Ensure MySQL is running and create a new database:**
    ```sql
      CREATE DATABASE PFSITE;

6. Initialize the database schema:
    ```bash
      python3 models/engine/storage_engine.py
    
7.Run the application:
```bash
      python3 app.py




