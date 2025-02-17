import requests
# Function to fetch book data from Open Library API
def fetch_books(query):
    search_url = f"https://openlibrary.org/search.json?q={query}&limit=10"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        data = response.json()
        books = []
        
        for doc in data.get("docs", []):
            work_key = doc.get("key", "")
            description = "No description available"
            
            if work_key:
                work_url = f"https://openlibrary.org{work_key}.json"
                work_response = requests.get(work_url)
                if work_response.status_code == 200:
                    work_data = work_response.json()
                    if "description" in work_data:
                        if isinstance(work_data["description"], dict):
                            description = work_data["description"].get("value", "No description available")
                        else:
                            description = work_data["description"]
            
            books.append({
                "title": doc.get("title", "Unknown"),
                "author": ", ".join(doc.get("author_name", ["Unknown"])),
                "description": description
            })
        
        return books
    return []