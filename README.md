# Aforro Backend – Django Assignment

This repository contains a complete backend implementation for the Aforro assignment using Django, PostgreSQL, Redis, Celery, and Docker.

The project is designed so that reviewers can **unzip the code and run it locally with minimal setup.

---

## Tech Stack

- Python 3.11
- Django
- PostgreSQL
- Redis
- Celery
- Docker & Docker Compose

---

## Project Structure

aforro-backend/
├── apps/
│ ├── products/
│ ├── stores/
│ ├── orders/
│ ├── search/
│ └── tests/
├── project/
│ ├── settings.py
│ ├── urls.py
│ ├── celery.py
│ └── wsgi.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md


---

## Features Implemented

- Product, Store, Inventory, and Order models
- Order creation API
- Asynchronous order processing using Celery
- Redis used as Celery broker (extensible for caching / rate limiting)
- Database seed command
- Django Admin interface
- Dockerized development environment
- Automated tests

---

## Setup Instructions (Step-by-Step)

### Step 1: System Requirements

Make sure Docker and Docker Compose are installed.

Verify using:

docker --version
docker compose version


## Step 2: Unzip the Project

After downloading the submission ZIP file:

unzip aforro-backend-submission.zip
cd aforro-backend



### Step 3: Start All Services Using Docker

This command starts:

1.Django web server

2.PostgreSQL database

3.Redis

4.Celery worker

docker compose up --build -d



### Step 4: Apply Database Migrations

docker compose exec web python manage.py migrate



### Step 5: Create Admin User

docker compose exec web python manage.py createsuperuser

### Admin Access:
Django admin is enabled. Reviewers can create their own admin user using

docker compose exec web python manage.py createsuperuser



### Step 6: Seed Sample Data

docker compose exec web python manage.py seed_data



### Step 7: Run Tests

docker compose exec web python manage.py test



### Step 8: Accessing the Application

## Django Admin Panel

http://localhost:8000/admin/



## Check Order API of JSON Response (Async via Celery)

http://localhost:8000/orders/create/

# Sample Response: 

{
  "message": "Order received",
  "task_id": "celery-task-id"
}



### Step 9: Docker Usage Summary

# Start services

docker compose up -d

# Stop services

docker compose down

# View logs

docker compose logs web
docker compose logs celery



### Scalability Considerations

- Celery allows horizontal scaling of background workers

- Redis supports caching and rate limiting

- PostgreSQL schema supports inventory consistency

- Dockerized setup simplifies cloud deployment
