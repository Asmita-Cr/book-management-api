# 📚 Book Recommendation

## 📌 Description
A full-stack project using only HTML forms and Flask to add books, review them, and get recommendations.

## Tech Stack
- Flask (Python)
- SQLite
- HTML, CSS
- Pytest + Coverage

## Running the Project
1. Clone the repo and navigate to the folder
2. Create virtual env and install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
python app.py
```
4. Visit `http://localhost:5000`

## Key Endpoints

| Method   | Endpoint          | Description                           |
|----------|-------------------|---------------------------------------|
| `GET`    | `/api/books`      | Fetch all books                       |
| `GET`    | `/api/books/<id>` | Fetch a single book by ID             |
| `POST`   | `/api/books`      | Add a new book                        |
| `PUT`    | `/api/books/<id>` | Update an existing book               |
| `DELETE` | `/api/books/<id>` | Delete a book                         |
| `GET`    | `/`               | Render homepage with book list (HTML) |
| `POST`   | `/books`          | Add a book via form (HTML frontend)   |


## Database Used & Integration
-Database: SQLite (books.db)
-Library: SQLAlchemy (ORM)

The Book model has:
-id: Integer, primary key
-title: String (required)
-author: String (required)
-genre: String (optional)
-year: Integer (optional)

## Technologies Used
- Python
- Flask
- SQLite
- HTML/CSS (Jinja templates)
- Pytest + Coverage

## How to run the server
-install the dependencies
pip install -r requirements.txt
-run the server
python app.py

The app will run on: http://localhost:5000/

## Frontend
Visit http://localhost:5000/ to:
View a list of books (rendered using index.html)
Add a new book using the form (POSTs to /books)
No additional steps needed for frontend — it's integrated.

## How to Interact with Your API
My API is a RESTful interface built using Flask. You can perform Create, Read, Update, and Delete (CRUD) operations on a collection of books.

You can use:
A browser (for GET requests)
Postman or curl for testing (I have used Curl in Powershell and these are the commands)
Any frontend or script using HTTP libraries like fetch, axios, or requests

1. GET ALL BOOKS
   =curl.exe http://localhost:5000/api/books

2. GET A BOOK BY ID: at the end add the book id
   =curl.exe http://localhost:5000/api/books/1

3. POST A NEW BOOK
-   $body = @{
-    title = "1984"
-    author = "Orwell"
-    genre = "Dystopian"
-    year  = 1949
-} | ConvertTo-Json -Compress

-Invoke-RestMethod -Uri http://127.0.0.1:5000/api/books -Method Post -Body $body -ContentType "application/json"

4. PUT TO UPDATE A BOOK: in the first line just before the last slash add the book number
   -curl.exe -X PUT http://localhost:5000/api/books/2 \
-H "Content-Type: application/json" \
-d '{"title":"The Silent Patient (Updated)", "year":2020}'

5. DELETE A BOOK: in the end add id of the book you want to delete
   =curl.exe -X DELETE http://localhost:5000/api/books/2

API Integrated:
This project includes a RESTful Book Recommendation API built with Flask. It supports full CRUD operations, along with a /recommend endpoint for generating mock recommendations based on a query

How to Run Tests:
pytest --cov=.

Test Coverage Screenshot:
![image](https://github.com/user-attachments/assets/d4f84586-e3e4-4866-8989-982fb2a48476)
![image](https://github.com/user-attachments/assets/718221e5-8ae2-4414-b32a-8f9f5d70efaf)
Thank You!!



