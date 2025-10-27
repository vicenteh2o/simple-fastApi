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
├── requirements.txt                           # Project dependencies
├── readme.md                                  # Project documentation
└── simple fastAPI.postman_collection.json    # Postman collection for API testing
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vicenteh2o/simple-fastApi.git
cd simple-fastApi
```

2. Install all dependencies:

```bash
pip3 install -r requirements.txt
```

**Alternative installation (manual):**

```bash
# Main dependencies
pip3 install fastapi uvicorn

# Testing dependencies (optional)
pip3 install pytest httpx
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

## Testing

### Automated Testing with pytest

The project supports automated testing using pytest and httpx. Create test files to test your API endpoints:

```bash
# Run all tests
python3 -m pytest

# Run tests with verbose output
python3 -m pytest -v

# Run specific test file
python3 -m pytest test_main.py
```

### Testing with Postman

A Postman collection is included in the project (`simple fastAPI.postman_collection.json`). Import this collection into Postman to test all API endpoints easily.

## Development

### Project Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation using Python type annotations

### Testing Dependencies

- **pytest**: Testing framework for Python applications
- **httpx**: Async HTTP client for testing FastAPI applications

### Local Development

```bash
# Install in development mode with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Setting Up Pre-commit Hook

To ensure code quality and run tests automatically before each commit, you can set up a pre-commit hook:

1. Create the pre-commit hook file:

```bash
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
echo "🔍 Running FastAPI tests with pytest..."
python3 -m pytest --maxfail=1 --disable-warnings -q
RESULT=$?

if [ $RESULT -ne 0 ]; then
  echo "❌ Tests failed after commit."
else
  echo "✅ All tests passed!"
fi
EOF
```

2. Make the pre-commit hook executable:

```bash
chmod +x .git/hooks/pre-commit
```

Now, every time you commit changes, the hook will automatically run your tests. If any tests fail, the commit will be prevented, ensuring that only working code is committed to the repository.

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
