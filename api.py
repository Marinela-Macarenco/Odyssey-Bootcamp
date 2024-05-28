
import requests

# Assuming Flask app is running locally on port 5000
url = "http://localhost:5000"  
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)  # This will print the scraped data in JSON format
else:
    print("Failed to fetch data:", response.status_code)
