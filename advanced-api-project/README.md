# Advanced API Project

## Overview
This project demonstrates how to create custom views using Django REST Framework's generic views and mixins to handle CRUD operations efficiently.

## Models
- `Author`: Stores author information.
- `Book`: Stores book information linked to an `Author`.

## API Endpoints
- `GET /api/books/`: List all books.
- `POST /api/books/`: Create a new book (authenticated users only).
- `GET /api/books/<int:pk>/`: Retrieve a single book by ID.
- `PUT /api/books/<int:pk>/`: Update a book by ID (authenticated users only).
- `DELETE /api/books/<int:pk>/`: Delete a book by ID (authenticated users only).

## Permissions
- Unauthenticated users can only view book information.
- Authenticated users can create, update, and delete books.


## API Query Examples
- **Filter by Title:** `/api/books/?title=SampleTitle`
- **Search by Keyword:** `/api/books/?search=Sample`
- **Order by Publication Year:** `/api/books/?ordering=publication_year`
- **Order by Title (Descending):** `/api/books/?ordering=-title`

