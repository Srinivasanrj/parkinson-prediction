import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

# Send request to the website 
url = "https://quotes.toscrape.com/" 
response = requests.get(url) 

if response.status_code == 200: 
    print("Page fetched successfully!") 
else: 
    print("Error fetching page") 
    exit() 

# Parse HTML 
soup = BeautifulSoup(response.text, 'html.parser') 

# Extract data 
quotes = [] 
for quote_div in soup.find_all('div', class_='quote'): 
    text = quote_div.find('span', class_='text').text 
    author = quote_div.find('small', class_='author').text 
    tags = [tag.text for tag in quote_div.find_all('a', class_='tag')]
    
    quotes.append({
        'Quote': text, 
        'Author': author, 
        'Tags': ', '.join(tags)
    }) 

# Save to DataFrame and CSV 
df = pd.DataFrame(quotes) 
print(df.head(10)) 
df.to_csv('quotes_scraped.csv', index=False) 
print("Data saved to quotes_scraped.csv")