import json
import os
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://fredderf:fred555@cluster0.a03do.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['scrap']

def scrape_quotes():
    quotes_list = []
    authors_list = []
    url = "http://quotes.toscrape.com/"
    
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author_name = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            
            quotes_list.append({
                "author": author_name,
                "quote": text,
                "tags": tags
            })
            
            if author_name not in [author['fullname'] for author in authors_list]:
                author_url = quote.find('small', class_='author').find_parent('div').find('a')['href']
                author_response = requests.get(url + author_url)
                author_soup = BeautifulSoup(author_response.text, 'html.parser')

                born_date = author_soup.find('span', class_='author-born-date')
                born_location = author_soup.find('span', class_='author-born-location')
                description = author_soup.find('div', class_='author-description')

                authors_list.append({
                    "fullname": author_name,
                    "born_date": born_date.get_text() if born_date else "Unknown",
                    "born_location": born_location.get_text() if born_location else "Unknown",
                    "description": description.get_text().strip() if description else "No description available."
                })

        next_button = soup.find('li', class_='next')
        url = url + next_button.find('a')['href'] if next_button else None

    # Перевірочка на існування папки, якщо нема створюємо
    if not os.path.exists('data'):
        os.makedirs('data')

    with open(os.path.join('data', 'quotes.json'), 'w', encoding='utf-8') as quotes_file:
        json.dump(quotes_list, quotes_file, ensure_ascii=False, indent=4)
    
    with open(os.path.join('data', 'authors.json'), 'w', encoding='utf-8') as authors_file:
        json.dump(authors_list, authors_file, ensure_ascii=False, indent=4)

    print("\n👍 Скрапінг готовий! Створено data/quotes.json + data/authors.json.")

def load_authors():
    try:
        authors_path = os.path.join('data', 'authors.json')
        with open(authors_path, 'r', encoding='utf-8') as file:
            authors = json.load(file)
            for author in authors:
                db.authors.insert_one({
                    'fullname': author['fullname'],
                    'born_date': author['born_date'],
                    'born_location': author['born_location'],
                    'description': author['description'],
                })
        return True
    except Exception as e:
        print(f"\nПомилка у авторах: {e}\n")
        return False

def load_quotes():
    try:
        quotes_path = os.path.join('data', 'quotes.json')
        with open(quotes_path, 'r', encoding='utf-8') as file:
            quotes = json.load(file)
            author_map = {author['fullname']: author['_id'] for author in db.authors.find()}
            
            quote_data = []
            for quote in quotes:
                author_id = author_map.get(quote['author'])
                if author_id:
                    quote_data.append({
                        'text': quote['quote'],
                        'author': ObjectId(author_id),
                        'tags': quote.get('tags', [])
                    })
            db.quotes.insert_many(quote_data)
        return True
    except Exception as e:
        print(f"\nПомилка у нотатках: {e}\n")
        return False

scrape_quotes()

if load_authors() and load_quotes():
    print("\n👍 Все завантажено у MongoDB!\n")
else:
    print("Щось пішло не так")
