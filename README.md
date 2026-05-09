# Academic Management API

REST API for academic management built with Python and FastAPI.

This project provides a backend system for managing students, courses, enrollments, and academic records through a scalable API architecture.

---

# Features

* Student registration and management
* Course creation and control
* Enrollment system
* CRUD operations
* RESTful API architecture
* JWT authentication
* Database integration
* Input validation with Pydantic

---

# Tech Stack

* Python
* FastAPI
* MySQL
* SQLAlchemy
* JWT Authentication
* Pydantic
* Docker
* Git

---

# Project Structure

```bash
Academic-Management-API/
│
├── app/
│   ├── routes/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── database/
│   └── main.py
│
├── requirements.txt
├── Dockerfile
└── README.md
```

# API Endpoints

## Students

* `GET /students`
* `POST /students`
* `PUT /students/{id}`
* `DELETE /students/{id}`

## Courses

* `GET /courses`
* `POST /courses`
* `PUT /courses/{id}`
* `DELETE /courses/{id}`

## Enrollments

* `POST /enrollments`
* `GET /enrollments`

---

# Installation

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Academic-Management-API.git
```

## Access the project folder

```bash
cd Academic-Management-API
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
uvicorn app.main:app --reload
```

---

# Docker

## Build the container

```bash
docker build -t academic-api .
```

## Run the container

```bash
docker run -p 8000:8000 academic-api
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

ReDoc:

```bash
http://127.0.0.1:8000/redoc
```

---

# Future Improvements

* Role-based access control
* Email notifications
* PostgreSQL support
* Automated testing
* CI/CD pipeline
* Docker Compose integration

---

# Author

Gabriel Borges

Backend Developer focused on APIs and AI-powered applications.
