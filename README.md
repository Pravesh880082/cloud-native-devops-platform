# 🚀 Cloud-Native DevOps Platform

A containerized FastAPI application with PostgreSQL, Docker, GitHub Actions CI/CD, Docker Hub, and automated deployment to AWS EC2.

This project demonstrates a practical **DevOps workflow** where application code is automatically tested, containerized, pushed to a Docker registry, and deployed to an AWS EC2 server.

---

## 📌 Project Overview

The **Cloud-Native DevOps Platform** is a backend application built with **FastAPI** and **PostgreSQL**.

The main goal of this project is to demonstrate an end-to-end DevOps pipeline:

```text
Developer
    │
    ▼
  GitHub
    │
    ▼
GitHub Actions
    │
    ├── CI
    │
    └── Docker Build & Push
              │
              ▼
          Docker Hub
              │
              ▼
           AWS EC2
              │
        ┌─────┴─────┐
        ▼           ▼
     FastAPI    PostgreSQL
     Docker       Docker
```

---

## ✨ Features

- ⚡ FastAPI REST API
- 🐘 PostgreSQL database
- 🐳 Docker containerization
- 🔗 Docker Compose for local development
- 📦 Docker Hub image registry
- 🔄 GitHub Actions CI/CD
- ☁️ AWS EC2 deployment
- ❤️ Application health check
- 🗄️ Database health check
- 📝 Task creation and retrieval APIs
- 🔐 GitHub Secrets for deployment credentials
- 🔁 Automated Docker image deployment to EC2

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| FastAPI | REST API framework |
| PostgreSQL | Database |
| Docker | Containerization |
| Docker Compose | Local multi-container environment |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | CI/CD automation |
| Docker Hub | Container image registry |
| AWS EC2 | Cloud deployment |
| Linux | Server environment |

---

## 📂 Project Structure

```text
cloud-native-devops-platform/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── docker-image.yml
│       └── deploy.yml
│
├── app/
│   └── main.py
│
├── tests/
│
├── terraform/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

# ⚙️ Application

The backend is built using FastAPI.

### Available endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application status |
| GET | `/health` | Application health check |
| GET | `/db-health` | Database connectivity check |
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a new task |

---

## 🔍 API Examples

### Application Status

```http
GET /
```

Response:

```json
{
  "message": "Cloud-Native DevOps Platform is running!"
}
```

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

### Database Health

```http
GET /db-health
```

Response:

```json
{
  "database": "connected"
}
```

### Get Tasks

```http
GET /tasks
```

Example response:

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Learn DevOps",
      "completed": false
    }
  ]
}
```

### Create Task

```http
POST /tasks?title=Learn%20DevOps
```

Example response:

```json
{
  "message": "Task created",
  "id": 1,
  "title": "Learn DevOps"
}
```

---

# 🐳 Docker

The application is packaged as a Docker image.

### Build the image

```bash
docker build -t cloud-native-devops-platform:1.0 .
```

### Run the application

```bash
docker run -d \
  --name devops-app \
  -p 8000:8000 \
  cloud-native-devops-platform:1.0
```

The application runs on:

```text
http://localhost:8000
```

FastAPI Swagger documentation:

```text
http://localhost:8000/docs
```

---

# 🐘 PostgreSQL

PostgreSQL is used as the application's persistent database.

The Docker Compose configuration creates a PostgreSQL container with:

```text
Database: devopsdb
Username: devops
Password: devops123
```

> For production environments, database credentials should be stored using environment variables or a dedicated secrets-management system rather than being committed to source code.

---

# 🔗 Docker Compose

The project includes Docker Compose for running the application and database together during local development.

Start the services:

```bash
docker compose up -d --build
```

Check running containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

Stop the services:

```bash
docker compose down
```

---

# 🔄 CI/CD Pipeline

GitHub Actions automates the build and deployment process.

The pipeline follows:

```text
Code Push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Install Dependencies
    │
    ├── Application Check
    │
    ├── Build Docker Image
    │
    └── Push Image to Docker Hub
                │
                ▼
            Docker Hub
                │
                ▼
             AWS EC2
                │
                ├── Pull Latest Image
                ├── Stop Old Container
                ├── Start New Container
                └── Run Health Checks
```

---

## 🧪 Continuous Integration

The CI workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies.
4. Checks the application source code.

Example workflow:

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```

---

# 🐳 Docker Image Pipeline

After code is pushed to the `main` branch, GitHub Actions builds the Docker image and pushes it to Docker Hub.

Docker image:

```text
pravesh880082/cloud-native-devops-platform:latest
```

Docker Hub:

**https://hub.docker.com/r/pravesh880082/cloud-native-devops-platform**

---

# ☁️ AWS EC2 Deployment

The application is deployed to an AWS EC2 Linux server.

The EC2 server runs:

```text
Docker
   │
   ├── FastAPI Container
   │
   └── PostgreSQL Container
```

The deployment workflow automatically:

1. Connects to EC2.
2. Pulls the latest Docker image.
3. Removes the previous application container.
4. Starts the latest application container.
5. Checks the application.
6. Checks the health endpoint.

Example deployment command:

```bash
sudo docker pull pravesh880082/cloud-native-devops-platform:latest

sudo docker rm -f devops-app || true

sudo docker run -d \
  --name devops-app \
  --network devops-network \
  -p 8000:8000 \
  pravesh880082/cloud-native-devops-platform:latest
```

---

# 🔐 GitHub Secrets

Sensitive deployment credentials are stored using **GitHub Actions Secrets**.

The project uses secrets such as:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
EC2_HOST
EC2_USERNAME
EC2_SSH_KEY
```

Sensitive values are **not stored in the GitHub repository**.

---

# ❤️ Deployment Health Checks

The deployment pipeline verifies the application after deployment.

### Application check

```bash
curl -f http://localhost:8000/
```

### Health check

```bash
curl -f http://localhost:8000/health
```

If either check fails, the deployment workflow reports a failure.

---

# 🧪 Local Testing

After starting the application, test:

```bash
curl http://localhost:8000/
```

```bash
curl http://localhost:8000/health
```

```bash
curl http://localhost:8000/db-health
```

```bash
curl http://localhost:8000/tasks
```

Create a task:

```bash
curl -X POST "http://localhost:8000/tasks?title=Learn%20DevOps"
```

---

# 📊 DevOps Workflow

This project demonstrates the following DevOps practices:

### 1. Version Control

Git and GitHub are used to manage application source code.

### 2. Continuous Integration

GitHub Actions automatically checks the application whenever changes are pushed.

### 3. Containerization

Docker packages the application and its dependencies into a portable container.

### 4. Container Registry

Docker Hub stores the built Docker image.

### 5. Continuous Deployment

GitHub Actions automatically deploys the latest image to AWS EC2.

### 6. Infrastructure Environment

AWS EC2 provides the cloud compute environment.

### 7. Health Monitoring

Automated health checks verify that the deployed application is responding correctly.

---



# 🚀 How to Run the Project

## 1. Clone the repository

```bash
git clone https://github.com/Pravesh880082/cloud-native-devops-platform.git
```

```bash
cd cloud-native-devops-platform
```

## 2. Start the application

```bash
docker compose up -d --build
```

## 3. Check containers

```bash
docker compose ps
```

## 4. Open the API

```text
http://localhost:8000
```

## 5. Open Swagger

```text
http://localhost:8000/docs
```

---

# 🔮 Future Improvements

Possible future improvements include:

- Kubernetes deployment
- Terraform infrastructure automation
- Prometheus monitoring
- Grafana dashboards
- Centralized logging
- HTTPS with a reverse proxy
- Application authentication
- Database migrations
- Automated unit and integration tests
- Kubernetes-based scaling
- AWS load balancing
- AWS managed database integration

---

# 🎯 Learning Outcomes

Through this project, I practiced:

- Building REST APIs with FastAPI
- Working with PostgreSQL
- Containerizing applications with Docker
- Managing multi-container applications
- Using Git and GitHub
- Creating CI/CD pipelines with GitHub Actions
- Publishing Docker images to Docker Hub
- Deploying applications on AWS EC2
- Working with Linux servers
- Managing deployment secrets
- Implementing deployment health checks
- Troubleshooting cloud and container environments

---

# 👨‍💻 Author

## Pravesh Kumar

Aspiring DevOps / Cloud Engineer

Interested in:

- ☁️ Cloud Computing
- 🚀 DevOps
- 🐳 Docker
- 🔄 CI/CD
- ☁️ AWS
- 🐧 Linux
- 🔐 Cloud Security
- 🛠️ Infrastructure Automation

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Built to learn. Built to deploy. Built to improve. 🚀**
