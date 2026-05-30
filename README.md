# Academic Management API

A RESTful API for academic management built with Python and FastAPI.

This project provides a scalable backend solution for managing students, courses, enrollments, and academic records through a modern API architecture.

---

# Features

* Student registration and management
* Course creation and management
* Enrollment management system
* Full CRUD operations
* RESTful API architecture
* JWT-based authentication
* Database integration
* Data validation with Pydantic
* Scalable and modular structure

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

---

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

* `GET /enrollments`
* `POST /enrollments`

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Academic-Management-API.git
```

## Navigate to the Project Directory

```bash
cd Academic-Management-API
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

---

# Docker

## Build the Docker Image

```bash
docker build -t academic-api .
```

## Run the Docker Container

```bash
docker run -p 8000:8000 academic-api
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# Future Improvements

* Role-Based Access Control (RBAC)
* Email notification system
* PostgreSQL support
* Automated testing
* CI/CD pipeline integration
* Docker Compose setup
* API rate limiting
* Audit logging

---

# Author

**Gabriel Borges**

Backend Developer focused on API development, software architecture, and AI-powered applications.
