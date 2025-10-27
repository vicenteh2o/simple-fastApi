# Simple FastAPI Project

A simple REST API built with FastAPI for managing items (todo-like functionality).

## Features

- ✅ Create items with text and completion status
- ✅ List all items with optional limit
- ✅ Get specific item by ID
- ✅ Automatic API documentation with Swagger UI and ReDoc
- ✅ Type validation with Pydantic models

## Project Structure

```
fastAPI/
├── main.py                                    # Main FastAPI application
├── item.py                                    # Pydantic models
├── readme.md                                  # Project documentation
└── simple fastAPI.postman_collection.json    # Postman collection for API testing
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vicenteh2o/simple-fastApi.git
cd simple-fastApi
```

2. Install dependencies:

```bash
pip3 install fastapi uvicorn
```

## Running the Application

Start the development server:

```bash
python3 -m uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### Root Endpoint

- **GET** `/` - Returns a welcome message

### Items Management

- **POST** `/items` - Create a new item
- **GET** `/items` - List all items (with optional limit parameter)
- **GET** `/items/{item_id}` - Get a specific item by ID

## Data Models

### Item

```json
{
  "text": "string",
  "is_done": false
}
```

## Example Usage

### Create an Item

```bash
curl -X POST "http://127.0.0.1:8000/items" \
     -H "Content-Type: application/json" \
     -d '{"text": "Learn FastAPI", "is_done": false}'
```

### Get All Items

```bash
curl -X GET "http://127.0.0.1:8000/items"
```

### Get All Items with Limit

```bash
curl -X GET "http://127.0.0.1:8000/items?limit=5"
```

### Get Specific Item

```bash
curl -X GET "http://127.0.0.1:8000/items/0"
```

## Testing with Postman

A Postman collection is included in the project (`simple fastAPI.postman_collection.json`). Import this collection into Postman to test all API endpoints easily.

## Development

### Project Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation using Python type annotations

### Local Development

```bash
# Install in development mode with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Response Examples

### Successful Item Creation

```json
[
  {
    "text": "Learn FastAPI",
    "is_done": false
  }
]
```

### Error Response (Item Not Found)

```json
{
  "detail": "Item 5 not found"
}
```
