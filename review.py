import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import streamlit as st
import pandas as pd
import sqlite3

def scrape_reviews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    reviews = []
    title = soup.find("div", class_="section-title-article pl-3 border-l-4 border-green-500").text.strip()
    paragraphs = soup.find_all("p")
    if paragraphs:
        content = paragraphs[-1].text.strip()
        reviews.append({"Title": title, "Content": content})
    else:
        reviews.append({"Title": title, "Content": "No reviews found."})
    return reviews

def analyze_sentiment(review):
    classifier = pipeline("sentiment-analysis")
    result = classifier(review)
    return result[0]['label']

def create_database(reviews):
    conn = sqlite3.connect("porsche_reviews.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reviews
                 (title TEXT, content TEXT, sentiment TEXT)''')
    
    for review in reviews:
        c.execute("SELECT COUNT(*) FROM reviews WHERE content = ?", (review["Content"],))
        if c.fetchone()[0] == 0:
            sentiment = analyze_sentiment(review["Content"])
            c.execute("INSERT INTO reviews (title, content, sentiment) VALUES (?, ?, ?)",
                      (review["Title"], review["Content"], sentiment))
    conn.commit()
    conn.close()

def main():
    st.title("Porsche Reviews ")
    st.write("Welcome to the Porsche Reviews!")
    st.image("images/easteregg.jpeg", caption="Porsche & Sigmoid")

    st.header("Display Reviews")
    conn = sqlite3.connect("porsche_reviews.db")
    df = pd.read_sql_query("SELECT * FROM reviews", conn)
    st.dataframe(df)

    st.header("Add Review")
    title = st.text_input("Title:")
    content = st.text_area("Content:")
    if st.button("Add Review"):
        if title and content:
            conn = sqlite3.connect("porsche_reviews.db")
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM reviews WHERE content = ?", (content,))
            if c.fetchone()[0] == 0:
                sentiment = analyze_sentiment(content)
                c.execute("INSERT INTO reviews (title, content, sentiment) VALUES (?, ?, ?)",
                          (title, content, sentiment))
                conn.commit()
                st.success("Review added successfully!")
            else:
                st.error("Review with this content already exists.")
            conn.close()
        else:
            st.error("Please provide both title and content for the review.")

    conn.close()
