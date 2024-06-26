Book Management API with FastAPI and Docker
This repository contains a FastAPI application for managing a collection of books. It provides functionalities for creating, reading, updating, and deleting books through a RESTful API. Additionally, the application is Dockerized for easy deployment.

Prerequisites
Python 3.9 or later (https://www.python.org/downloads/)
Docker Desktop (https://www.docker.com/products/docker-desktop)
Installation
1. Setting Up the Environment:

Clone this repository using Git:

Bash
git clone https://github.com/nwaosa19/book_api.git

Navigate to the project directory:

Bash
cd book_api
1. Install Dependencies:

Install the required Python libraries using pip:

Bash
pip install -r requirements.txt
3. Run the Application (Using Uvicorn):

Run the following command to start the FastAPI development server:

Bash
uvicorn main:app --host 0.0.0.0 --port 8000
This command starts the Uvicorn server using the main.py file as the entry point and the app instance as the FastAPI application.
--host 0.0.0.0 allows connections from all interfaces.
--port 8000 sets the port for the server (you can change this if needed).
4. Run the Application (Using Docker):

a. Build the Docker Image:

```bash
docker build -t book_api .
```

- This command builds a Docker image named `book_api` from the Dockerfile in the current directory.
b. Run the Container:

```bash
docker run -p 8000:8000 book_api
```

- This command runs a container from the `book_api` image and maps the container's port 8000 to the host machine's port 8000.
- Now you can access the API at `http://localhost:8000/docs`.
Usage
The API provides the following endpoints for managing books:

1. Get All Books ([GET] /books):

Retrieves a list of all books in the collection.
Response: JSON array containing book objects. Each book object includes:
id (integer): Unique identifier for the book.
title (string): Title of the book.
author (string): Author of the book.
year (integer): Year of publication.
isbn (string): ISBN number of the book.
2. Get a Specific Book ([GET] /books/{book_id}):

Retrieves information about a book based on its ID.
Path Parameter:
{book_id}: Integer representing the unique ID of the book.
Response: JSON object containing the book details (same structure as Get All Books response for a single book).
Error: If the book with the specified ID is not found, a 404 Not Found error is returned.
3. Create a New Book ([POST] /books):

Creates a new book in the collection.
Request Body: JSON object with the following properties:
title (string): Required. Title of the book.
author (string): Required. Author of the book.
year (integer): Required. Year of publication.
isbn (string): Required. ISBN number of the book.
Response: JSON object containing the newly created book details (same structure as Get All Books response for a single book).
Error: If required fields are missing or data types are invalid, a 400 Bad Request error is returned.
4. Update a Book ([PUT] /books/{book_id}):

Updates information about an existing book.
Path Parameter:
{book_id}: Integer representing the unique ID of the book.
Request Body: JSON object containing any or all of the following properties (only the provided fields will be updated):
title (string): Title of the book.
author (string): Author of the book.
year (integer): Year of publication.
