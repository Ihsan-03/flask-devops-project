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

# Run the Project
-pip install -r requirements.txt
-python3 app.py

# API 
GET    /items        → Get all items
POST   /items        → Create item
PUT    /items/<id>   → Update item
DELETE /items/<id>   → Delete item
GET    /health       → Health check

# Example
curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"name":"Ihsan"}'

# Project Structure
├──  app.py
├──  Dockerfile
├──  requirements.txt
├── .gitignore
├── .dockerignore
└──  README.md
