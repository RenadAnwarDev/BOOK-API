# Book Management API

## 1. Project Overview

This project is a RESTful API for managing a collection of books. It allows users to create, retrieve, update, and delete books using simple HTTP requests. The API is built using FastAPI and stores data in a SQLite database.

## 2. Technologies Used

- Python 3.13
- FastAPI framework for building APIs
- SQLite database for local storage
- Uvicorn ASGI server to run the app

## 3. How to Run the Project Locally

1. Clone the repository:

```bash
git clone https://github.com/RenadAnwarDev/BOOK-API.git
cd BOOK-API
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the API server:

```bash
uvicorn main:app --reload
```

5. Open your browser and visit the API documentation:

```
http://127.0.0.1:8000/docs
```

## 4. API Endpoints

| Method | Endpoint           | Description               | Request Body                          | Response                      |
|--------|--------------------|---------------------------|-------------------------------------|-------------------------------|
| GET    | /api/books         | Retrieve all books (with pagination)        | None                                | List of book objects           |
| POST   | /api/books         | Create a new book (requires Basic Auth)         | JSON with title, author, publishedDate, numberOfPages | Created book object            |
| GET    | /api/books/{id}    | Get details of a book by ID (requires Basic Auth) | None                                | Book object                   |
| PUT    | /api/books/{id}    | Update a book by ID (requires Basic Auth)       | JSON with updated fields (title, numberOfPages) | Updated book object            |
| DELETE | /api/books/{id}    | Delete a book by ID (requires Basic Auth)       | None                                | Confirmation message          |

## 5. Screenshots of API Usage

- Swagger UI main interface (auto-generated documentation):

  ![Swagger UI](screenshots/swagger_ui_main.png)

- Basic Auth Login prompt:

  ![Basic Auth Login](screenshots/basic_auth_login.png)

- Create Book request example (with auth):

  ![Create Book](screenshots/post_create_book.p.png)

- Get All Books response example (with pagination):

  ![All Books](screenshots/get_all_books.p.png)

- Get Single Book example:

  ![Single Book](screenshots/get_single_book.png)

- Update Book request example:

  ![Update Book](screenshots/put_update_book.png)

- Delete Book request example:

  ![Delete Book](screenshots/delete_book.png)

## 6. API Documentation

This API uses FastAPI's built-in automatic documentation powered by Swagger UI. The documentation is accessible at:

```
http://127.0.0.1:8000/docs
```

From there, you can test all available endpoints interactively.

## 7. Bonus Features

### Basic Authentication (Basic Auth)

- Added Basic Authentication to secure the API endpoints.
- Users must provide a username and password (e.g., admin / 1234) to access any endpoint.
- Unauthorized users will receive a 401 Unauthorized error.
- This is implemented using FastAPI's `HTTPBasic` security scheme.

### Pagination

- Pagination is implemented on the endpoint that returns all books (`GET /api/books`).
- You can control pagination using query parameters:
  - `skip`: number of records to skip (default 0)
  - `limit`: number of records to return (default 10)
- Example: `/api/books?skip=10&limit=5` returns 5 books starting from the 11th record.

---

## 8. Additional Notes

- The database file `books.db` is created automatically on the first run.
- Make sure you have Python 3.7 or higher installed.
- The API is designed for learning and simple usage, not production-ready without additional security.

## 9. Contact and Repository

The source code is available at:

https://github.com/RenadAnwarDev/BOOK-API.git

Feel free to open issues or contribute.
