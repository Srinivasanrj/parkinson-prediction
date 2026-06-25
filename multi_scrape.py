import requests 
from bs4 import BeautifulSoup 
import pandas as pd 
import time 
all_books = [] 
base_url = "http://books.toscrape.com/catalogue/page-{}.html" 
for page in range(1, 4): 
    if page == 1: 
        url = "http://books.toscrape.com/" 
    else: 
        url = base_url.format(page) 
    response = requests.get(url) 
    soup = BeautifulSoup(response.text, 'html.parser') 

    for article in soup.find_all('article', class_='product_pod'): 
        title = article.h3.a['title'] 
        price = article.find('p', class_='price_color').text 
        all_books.append({'Title': title, 'Price': price, 'Page': page}) 
    print(f"Page {page} completed") 
time.sleep(1) 
df = pd.DataFrame(all_books) 
df.to_csv('books_multiple_pages.csv', index=False) 
print(f"Total books: {len(df)} → Saved!") 