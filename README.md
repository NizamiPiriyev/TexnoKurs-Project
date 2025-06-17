# TexnoKurs Documentation

## Introduction
TexnoKurs is a full-stack web application built using Python and Django that allows users to enroll in courses, make payments, post reviews, and manage their learning experience. The platform is designed to offer an intuitive and efficient way to explore educational content, featuring a keyword-based filtering system, secure authentication, and a responsive user interface.

## Technologies Used
TexnoKurs leverages a robust tech stack to ensure scalability, security, and usability:
- **Backend**: Python with the Django Framework, providing a high-level, secure, and maintainable structure for web development.
- **Frontend**: HTML for structure, CSS and Bootstrap for styling, and JavaScript for dynamic interactions, ensuring a responsive and user-friendly interface.
- **Database**: SQLite3 for development (lightweight and easy to set up), with PostgreSQL recommended for production due to its robustness and performance.
- **Authentication & Admin Customization**: Django’s built-in authentication system for secure user management, enhanced by the Jazzmin package for a modern admin interface.

## Architecture
TexnoKurs follows a three-tier architecture:
1. **Frontend**: Implements the UI using HTML, CSS, Bootstrap, and JavaScript for a responsive experience across devices.
2. **Backend**: Handles business logic, API endpoints, and database interactions using Django’s ORM and view system.
3. **Database**: Stores user data, course details, and transaction records using SQLite3, with scalability to PostgreSQL.


## Features Overview
1. **User Authentication**
   - Secure login and registration system
   - Password reset functionality
   - Session-based authentication using Django’s built-in features
2. **Course Management**
   - Users can browse, enroll, and delete courses
   - Courses categorized with keywords and tags for easy searching
   - Course details page with comprehensive information
3. **Payment System**
   - Secure payment processing for enrolling in courses
   - Supports multiple payment methods (credit cards, PayPal, etc.)
   - Ensures transaction security and data protection
4. **Comment System**
   - Users can post reviews and feedback on courses
   - Comments are moderated via the admin panel
   - Helps other users make informed decisions
5. **Course Filtering**
   - Keyword and tag-based filtering system
   - Allows users to quickly find relevant courses
6. **Admin Panel**
   - Custom admin dashboard powered by the Jazzmin package
   - Enables management of users, courses, payments, and comments
   - User-friendly interface for site administrators

## Getting Started
### 1. Installation & Setup
Ensure you have Python and Django installed. Clone the repository and navigate to the project folder:
```
git clone <https://github.com/NizamiPiriyev/TexnoKurs-Project>
cd TexnoKurses
```
Install dependencies:
```
pip install -r requirements.txt
```
Run migrations and start the development server:
```
python manage.py migrate
python manage.py runserver
```
Access the website at: http://127.0.0.1:8000/

### 2. File Structure
```
TexnoKurses/
├── TexnoKurs/
│   ├── account
│   ├── courses
│   ├── ...
├── env/
│   ├── Include
│   ├── Lib
│   ├── Scripts
│   ├── pyvenv
├── README.MD/

```
- `TexnoKurs/` – Main project settings and configurations
- `env/` – App enviroment folder

## Deployment
### Production Deployment Instructions
To deploy TexnoKurs in a production environment:
1. **Database Setup**:
   - Replace SQLite3 with PostgreSQL:
     ```
     pip install psycopg2
     ```
   - Update `settings.py` with PostgreSQL credentials.
2. **Web Server Configuration**:
   - Install and configure a web server like Nginx or Apache.
   - Set up a reverse proxy to forward requests to the application server.
3. **Application Server**:
   - Install Gunicorn:
     ```
     pip install gunicorn
     ```
   - Run with:
     ```
     gunicorn --bind 0.0.0.0:8000 texnocourse.wsgi:application
     ```
4. **Environment Variables**:
   - Use a `.env` file or system environment variables for sensitive data (e.g., `SECRET_KEY`, `DATABASE_URL`).
   - Example `.env`:
     ```
     SECRET_KEY=your-secret-key
     DATABASE_URL=postgres://user:password@localhost/dbname
     ```
5. **Security**:
   - Enable HTTPS with a certificate from Let’s Encrypt.
   - Configure Django’s `ALLOWED_HOSTS` in `settings.py`.

## Contributing
We welcome contributions! To contribute:
1. Fork the repository
2. Create a feature branch
3. Make improvements and submit a pull request

## Credits
TexnoKurs was developed by Nizami Piriyev as a full-stack educational platform. The project integrates modern web technologies to provide a seamless learning experience.

## Conclusion
TexnoKurs is a robust learning management system built with Django, offering secure authentication, payment processing, and an intuitive course management interface. Its scalable architecture supports future enhancements, such as AI-driven course recommendations and an advanced analytics dashboard for tracking user progress, making it a promising platform for online education.
