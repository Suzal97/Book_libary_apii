# Book Library API

This is a simple CRUD (Create, Read, Update, Delete) API for managing a collection of books in a library, built using FastAPI and MongoDB. The application allows users to perform operations on books, including creating new records, retrieving existing records, updating records, and deleting records.

## Features

- FastAPI framework for building the RESTful API.
- MongoDB for storing book records.
- Clean architecture with separation of concerns.
- Dockerized for easy deployment.
- Swagger and ReDoc for API documentation.

## Requirements

- Python 3.7+
- MongoDB (local or cloud instance)
- Docker (optional, for containerization)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Suzal97/Book_libary_apii.git
cd library-api

# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows
.\env\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pymongo

# Use Uvicorn to run the FastAPI application:
uvicorn app.main:app --reload

#Access the API Documentation
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc



