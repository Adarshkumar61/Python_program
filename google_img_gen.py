from googleapiclient.discovery import build
import os
import urllib.request

# API credentials
API_KEY = "YOUR_API_KEY"
CSE_ID = "YOUR_CSE_ID"

# Search query and parameters
query = "python programming"
search_type = "image"

# Create the API client
service = build("customsearch", "v1", developerKey=API_KEY)

# Perform the search
res = service.cse().list(q=query, cx=CSE_ID, searchType=search_type).execute()

# Download the images
for result in res["items"]:
    url = result["link"]
    path = os.path.join("images", os.path.basename(url))
    urllib.request.urlretrieve(url, path)
    print(f"Downloaded {url} to {path}")
