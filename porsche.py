from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

# Function to scrape data from an individual car model page
def scrape_model_data(model_url):
    response = requests.get(model_url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Initialize lists to store data for all models on the page
    model_names = []
    currencies = []
    chassis_list = []
    spans = []
    
    # Find all <tr> tags containing model information
    model_info_tags = soup.find_all("tr")
    
    # Loop through each <tr> tag to extract data for each model
    for tag in model_info_tags:
        # Extract model name from strong tag with class "tit"
        model_name_tag = tag.find("strong", class_="tit")
        model_name = model_name_tag.text.strip() if model_name_tag else "N/A"
        
        # Extract currency from strong tag with class "cur" or "end"
        currency_tag = tag.find("strong", class_=["cur", "end"])
        currency = currency_tag.text.strip() if currency_tag else "N/A"
        
        # Extract chassis from strong tag with class "chas"
        chassis_tag = tag.find("strong", class_="chas")
        chassis = chassis_tag.text.strip() if chassis_tag else "N/A"
        
        # Extract span from span tag
        span_tag = tag.find("span")
        span = span_tag.text.strip() if span_tag else "N/A"
        
        # Append extracted data to lists
        model_names.append(model_name)
        currencies.append(currency)
        chassis_list.append(chassis)
        spans.append(span)
    
    # Return a dictionary containing lists of data for all models on the page
    return {
        "Model Name": model_names,
        "Currency": currencies,
        "Chassis": chassis_list,
        "Span": spans
    }

# List of URLs to scrape
urls = [
    "https://www.auto-data.net/en/porsche-356-model-2874",
    "https://www.auto-data.net/en/porsche-718-model-2095",
    "https://www.auto-data.net/en/porsche-901-model-3400",
    "https://www.auto-data.net/en/porsche-911-model-724",
    "https://www.auto-data.net/en/porsche-912-model-2689",
    "https://www.auto-data.net/en/porsche-914-model-2690",
    "https://www.auto-data.net/en/porsche-917-model-2935",
    "https://www.auto-data.net/en/porsche-918-model-2055",
    "https://www.auto-data.net/en/porsche-924-model-729",
    "https://www.auto-data.net/en/porsche-928-model-734",
    "https://www.auto-data.net/en/porsche-944-model-725",
    "https://www.auto-data.net/en/porsche-959-model-730",
    "https://www.auto-data.net/en/porsche-968-model-726",
    "https://www.auto-data.net/en/porsche-boxster-model-731",
    "https://www.auto-data.net/en/porsche-carrera-gt-model-727",
    "https://www.auto-data.net/en/porsche-cayenne-model-732",
    "https://www.auto-data.net/en/porsche-cayman-model-728",
    "https://www.auto-data.net/en/porsche-macan-model-2056",
    "https://www.auto-data.net/en/porsche-mission-e-model-2374",
    "https://www.auto-data.net/en/porsche-mission-x-model-3325",
    "https://www.auto-data.net/en/porsche-panamera-model-733",
    "https://www.auto-data.net/en/porsche-taycan-model-2719"
]

# Initialize lists to store scraped data for all models
all_model_names = []
all_currencies = []
all_chassis = []
all_spans = []

# Loop through each URL to scrape data from all models on each page
for model_url in urls:
    # Scrape data from the model page
    model_info = scrape_model_data(model_url)
    # Append scraped data to corresponding lists
    all_model_names.extend(model_info["Model Name"])
    all_currencies.extend(model_info["Currency"])
    all_chassis.extend(model_info["Chassis"])
    all_spans.extend(model_info["Span"])

# Combine the scraped data into a list of dictionaries
porsche_models = []
for model_name, currency, chassis, span in zip(
        all_model_names, all_currencies, all_chassis, all_spans):
    porsche_models.append({
        "Model Name": model_name,
        "Currency": currency,
        "Chassis": chassis,
        "Span": span
    })

# Save the scraped data to a JSON file
df = pd.DataFrame({
    "Model Name": all_model_names,
    "Currency": all_currencies,
    "Chassis": all_chassis,
    "Span": all_spans
})
df.to_json("porsche_data.json", orient="records")

# Define API endpoint to serve the scraped data
@app.route("/porsche_models", methods=["GET"])
def get_porsche_models():
    return jsonify(porsche_models)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
