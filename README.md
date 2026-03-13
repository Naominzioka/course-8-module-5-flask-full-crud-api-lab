# Event Management RESTful API (Flask CRUD Lab)

## Overview
This project is a **RESTful API built with Flask** that allows users to manage events. The API supports **full CRUD operations**, meaning events can be created, updated, and deleted through HTTP requests.

The application simulates a database using **in-memory Python objects** and returns responses in **JSON format**.

## Technologies Used
- Python
- Flask
- RESTful API principles
- JSON for request and response data

## Features
- Create a new event
- Update an existing event
- Delete an event
- Return structured JSON responses
- Proper HTTP status codes for API responses

## API Endpoints

### Create Event
**POST /events**

Creates a new event.

Example request body:

```json
{
  "title": "Hackathon"
}
```

Example response:

```json
{
  "id": 3,
  "title": "Hackathon"
}
```

Status Code: `201 Created`

---

### Update Event
**PATCH /events/<id>**

Updates the title of an existing event.

Example request body:

```json
{
  "title": "Hackathon 2025"
}
```

Status Code: `200 OK`

---

### Delete Event
**DELETE /events/<id>**

Deletes an event by its ID.

Status Code: `204 No Content`

---

## Project Structure

```
project-folder
│
├── app.py        # Flask API implementation
└── README.md     # Project documentation
```

## How to Run the Project

1. Clone the repository

```bash
git clone <your-repo-url>
```

2. Navigate to the project folder

```bash
cd project-folder
```

3. Install dependencies

```bash
pip install flask
```

4. Run the Flask server

```bash
python app.py
```

The API will run on:

```
http://localhost:5000
```

## Testing the API

You can test the endpoints using:
- Postman
- curl
- Thunder Client (VS Code)

Example requests:

```
POST http://localhost:5000/events
PATCH http://localhost:5000/events/1
DELETE http://localhost:5000/events/1
```

## Notes
- This project uses **in-memory storage**, so data resets whenever the server restarts.
- It was built as part of a lab to practice **Flask REST API development and CRUD operations**.