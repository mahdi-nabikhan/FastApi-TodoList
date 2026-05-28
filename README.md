# Todo App - FastAPI & React

A modern Full-Stack Todo Application built with **FastAPI**, **React**, **JWT Authentication**, and **Docker Compose**.
This project combines a scalable backend API with a modern React frontend inside a unified project structure.

---

# 🚀 Features

## Backend (FastAPI)

* RESTful API architecture
* JWT Authentication & Authorization
* User Registration & Login
* Protected Routes
* CRUD operations for Todos
* SQLAlchemy ORM
* PostgreSQL Database
* Pydantic Validation
* Pytest Testing
* Environment Variables Support

## Frontend (React)

* React SPA Architecture
* Axios API Integration
* Authentication Flow
* Protected Routes
* Responsive UI
* Component-Based Structure

## DevOps

* Docker
* Docker Compose
* Containerized Development Environment

---

# 🛠 Tech Stack

## Backend

* FastAPI
* Python
* SQLAlchemy
* PostgreSQL
* JWT
* Pytest

## Frontend

* React
* JavaScript
* Axios
* React Router

## DevOps

* Docker
* Docker Compose

---

# 📂 Project Structure

```bash id="v5lq2h"
project/
│
├── src/
│   │
│   ├── backend/
│   │   ├── app/
│   │   ├── tests/
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   │
│   └── frontend/
│       ├── src/
│       ├── public/
│       ├── package.json
│       ├── Dockerfile
│       └── vite.config.js
│
├── docker-compose.yml
├── .env
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash id="9zjlwm"
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

---

# 🐳 Run with Docker Compose

Build and run all services:

```bash id="4vkk54"
docker-compose up --build
```

Run in detached mode:

```bash id="8hxcn8"
docker-compose up -d
```

Stop containers:

```bash id="z89s47"
docker-compose down
```

---

# 🔧 Backend Setup (Without Docker)

```bash id="1jlwmn"
cd src/backend

python -m venv venv

source venv/bin/activate
# Windows:
# venv\Scripts\activate

pip install -r requirements.txt
```

Run backend server:

```bash id="7oofg0"
uvicorn app.main:app --reload
```

---

# 💻 Frontend Setup (Without Docker)

```bash id="ndy7hl"
cd src/frontend

npm install
npm run dev
```

---

# 🧪 Run Tests

```bash id="mqyrp5"
cd src/backend

pytest
```

---

# 🔐 Authentication

This project uses **JWT Authentication** for securing API endpoints.

Features:

* User Registration & Login
* Access Token Authentication
* Protected Routes
* User-specific Todo Management

---

# 📌 API Endpoints

## Authentication

* `POST /register`
* `POST /login`

## Todo

* `GET /todos`
* `POST /todos`
* `PUT /todos/{id}`
* `DELETE /todos/{id}`

---

# 🌐 Services

| Service        | Description                   |
| -------------- | ----------------------------- |
| Backend        | FastAPI API Server            |
| Frontend       | React Application             |
| Database       | PostgreSQL                    |
| Docker Compose | Multi-container orchestration |

---

# 📈 Future Improvements

* Refresh Token Support
* Redis Caching
* Celery Background Tasks
* CI/CD Pipeline
* Kubernetes Deployment
* WebSocket Notifications

---

# 🤝 Contributing

Contributions, issues, and feature requests are welcome.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Developer

Built with ❤️ using FastAPI, React & Docker
