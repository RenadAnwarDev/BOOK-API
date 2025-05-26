# 📚 Book Management API

This is a simple RESTful API for managing a collection of books using **FastAPI** and **SQLite**.

---

## 🔧 Features

- Add a new book
- Retrieve a list of all books
- Get details of a specific book
- Update book details
- Delete a book
- Interactive API documentation with Swagger UI

---

## 🚀 Technology Stack

- Python 3.13  
- FastAPI  
- SQLite  
- Uvicorn (for running the server)

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/book-api.git
cd book-api
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

The API will be available at:  
👉 `http://127.0.0.1:8000`  
Swagger docs:  
👉 `http://127.0.0.1:8000/docs`

---

## 📸 Screenshots

### 🔹 Swagger UI

Shows all available endpoints.  
📷 `screenshots/swagger-ui.png`

---

### 🔹 Add Book (POST /api/books)

Request body:  
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "publishedDate": "1925-04-10",
  "numberOfPages": 180
}
```

Response:  
📷 `screenshots/post-add-book.png`

---

### 🔹 List All Books (GET /api/books)

Displays a list of all books.  
📷 `screenshots/get-all-books.png`

---

### 🔹 Get Book by ID (GET /api/books/{book_id})

Displays the details of a specific book.  
📷 `screenshots/get-book-by-id.png`

---

### 🔹 Update Book (PUT /api/books/{book_id})

Request body example:  
```json
{
  "title": "The Great Gatsby - Updated",
  "numberOfPages": 200
}
```

Response:  
📷 `screenshots/update-book.png`

---

### 🔹 Delete Book (DELETE /api/books/{book_id})

Deletes a book by ID.  
📷 `screenshots/delete-book.png`

---

## 📂 Project Structure

```
book-api/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── swagger-ui.png
    ├── post-add-book.png
    ├── get-all-books.png
    ├── get-book-by-id.png
    ├── update-book.png
    └── delete-book.png
```

---

## ✅ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/books | Get all books |
| POST   | /api/books | Add a new book |
| GET    | /api/books/{id} | Get a specific book |
| PUT    | /api/books/{id} | Update a book |
| DELETE | /api/books/{id} | Delete a book |

---

## 📌 Notes

- Make sure you have Python 3.13+ installed.
- This project is for demonstration and evaluation purposes.

---

## 🧑‍💻 Author

Created by Renad Al-Shahri  
🚀 Capstone Project — May 2025  