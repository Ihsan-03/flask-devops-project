# Flask DevOps Project

*AIM* - To Design and implement a complete DevOps pipeline and infrastructure to
deploy this application in a scalable and production-ready way.

# Description
This project is a simple Flask-based web application with a REST API (CRUD Based)
It is designed as part of a DevOps assignment and includes containerization using Docker

# Features

- Flask web application  
- REST API (CRUD-based)  
- Health check endpoint (/health)  
- Dockerized application  
- GitHub (version control)  

# Tech Stack
- Python  
- Flask  
- Flask-RESTful  
- Docker  
- mysql-connector-python

# Database Setup
1. Install MySQL
2. Open MySQL terminal:
   mysql -u root -p
3. Run the following:
   created Database assignment_db;
   use assignment_db;
   create table items (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) );

# Deployment
- Deployed on AWS EC-2 instance
- Runs on Port 5000
- http://<ec2-ip>:5000
- Configured Nginx for reverse proxy
- Nginx routes traffic 

# Run the Project
- pip install -r requirements.txt
- python3 app.py

# Docker Setup 
- Build image
      docker build -t flask-devops-app
- Run cantainer
      docker run -d -p 5000:5000 flask-devops-app
- Run applicaion on browser
      http://localhost:5000
- Stop cantainer
      docker ps
      docker stop <cantainer_id>
- Remove cantainer
      docker rm <cantainer_id>
- Remove image
      docker rmi flask-devops-app

# API 
GET    /items        → Get all items
POST   /items        → Create item
PUT    /items/<id>   → Update item
DELETE /items/<id>   → Delete item
GET    /health       → Health check

# Example

Local:
http://127.0.0.1:5000

To perform operations:
curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"name":"Ihsan"}'


AWS:
http://<ec2-IP>:5000

To perform operations:
curl -X POST http://<ec2-IP>:5000/items -H "Content-Type: application/json" -d '{"name":"Ihsan"}'


# Project Structure
├──  app.py
├──  Dockerfile
├──  requirements.txt
├── .gitignore
├── .dockerignore
└──  README.md

# Challenges faced
- pip installation issue
I got error related to environment management, which prevented pip from installing packages
Solution:-
I solved it by creating a virtual environment and installed dependencies

Commands used to resolve:
--> python3 -m venv venv
--> source venv/bin/activate
--> pip install flask flask-restful

- MySQL authentication issue
I was unable to connect using root user due to authentication errors (error 1698)
Solution:-
I used sudo mysql to login
Created a new MySQL user

- Database connection issues
Initially faced issues like:-
“Access denied”
“Cursor not connected”
Solution:-
Created a user and entered correct credentials
Created fresh DB 
Avoided global cursor

- Debugging API issues
API was working but wasn't fetching data
I was using old data instead of MySQL
Solution:-
Replaced old data with SQL queries

- Syntax and coding errors
