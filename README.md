# 🚀 Todo App - FastAPI & React

A modern Full-Stack Todo Application built with FastAPI, React, PostgreSQL, JWT Authentication, and Docker Compose.

This project demonstrates how to build a scalable web application using a modern backend architecture alongside a React frontend.

---

## ✨ Features

### Authentication

* User Registration
* User Login
* JWT Authentication
* Access & Refresh Tokens
* HTTPOnly Cookie Authentication
* Protected Routes

### Todo Management

* Create Todo
* Update Todo
* Delete Todo
* View Todo Details
* Pagination Support
* User-specific Todos

### Admin Panel

* Admin Dashboard
* User Management
* View User Details
* Delete Users
* Create Superusers

### Backend

* FastAPI
* SQLAlchemy ORM
* Alembic Migrations
* PostgreSQL
* Pydantic Validation
* Modular Project Structure
* Environment Variables
* Pytest Testing

### Frontend

* React
* React Router
* Custom Hooks
* Protected Pages
* Modal Components
* Responsive Design
* Dashboard UI

### DevOps

* Docker
* Docker Compose
* Containerized Environment

---

## 🏗 Architecture

```text
React Frontend
        │
        ▼
FastAPI Backend
        │
        ▼
 PostgreSQL
```

Authentication Flow:

```text
Login
  │
  ▼
Generate JWT Tokens
  │
  ▼
Store Tokens in HTTPOnly Cookies
  │
  ▼
Protected API Access
```

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* JWT
* Pytest

### Frontend

* React
* JavaScript
* React Router
* Fetch API
* CSS

### DevOps

* Docker
* Docker Compose

---

## 📂 Project Structure

```bash
src/
│
├── users/
├── tasks/
├── permissions/
├── core/
├── migrations/
│
├── frontend/
│   ├── Components/
│   ├── Hooks/
│   ├── Pages/
│   ├── Layouts/
│   └── Router/
│
└── tests/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/todo-app.git

cd todo-app
```

---

## 🐳 Run with Docker

Build containers:

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up -d
```

Stop containers:

```bash
docker compose down
```

---

## 🔧 Backend Development

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
source venv/bin/activate

# Windows

venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

---

## 💻 Frontend Development

```bash
npm install

npm run dev
```

---

## 🗄 Database Migrations

Create migration:

```bash
alembic revision --autogenerate -m "migration message"
```

Apply migration:

```bash
alembic upgrade head
```

---

## 🔐 Authentication

The application uses JWT Authentication with HTTPOnly Cookies.

### Access Token

Used for protected API requests.

### Refresh Token

Used to generate a new access token without requiring the user to log in again.

---

## 📌 Main API Endpoints

### Authentication

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /register      |
| POST   | /login/jwt     |
| POST   | /refresh_token |

### Tasks

| Method | Endpoint          |
| ------ | ----------------- |
| GET    | /tasks            |
| POST   | /tasks            |
| PUT    | /task/{id}        |
| DELETE | /delete/task/{id} |

### Admin

| Method | Endpoint          |
| ------ | ----------------- |
| GET    | /all/users        |
| GET    | /admin/users/{id} |
| DELETE | /admin/users/{id} |

---

## 🧪 Testing

Run all tests:

```bash
pytest
```

---

## 🚧 Future Improvements

* Redis Caching
* Celery Background Tasks
* Email Verification
* Password Reset
* Role-Based Permissions
* CI/CD Pipeline
* Kubernetes Deployment
* Nginx Reverse Proxy
* WebSocket Notifications

---

## 🤝 Contributing

Pull requests, issues, and feature suggestions are welcome.

---

## 📄 License

MIT License

---

## 👨‍💻 Developer

Built with ❤️ using FastAPI, React, PostgreSQL, Docker, and JWT Authentication.
