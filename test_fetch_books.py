from app import fetch_books
# Test the function
query = "Harry Potter"
books = fetch_books(query)

# Print results
for book in books:
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Description: {book['description']}")
    print("-" * 50)


