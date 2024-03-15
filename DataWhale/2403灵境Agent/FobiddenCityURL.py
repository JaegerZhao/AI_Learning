import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.dpm.org.cn/explore/buildings.html"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all building links
building_links = soup.find_all('a', href=True)

# Filter out links that do not contain '/explore/building/'
building_links = [link for link in building_links if '/explore/building/' in link['href']]

# Open a file to write the building names and URLs
with open('building_links.txt', 'w', encoding='utf-8') as file:
    # Format and write the building names and URLs to the file
    for link in building_links:
        building_name = link.text.strip()
        building_url = f"https://www.dpm.org.cn{link['href']}"
        file.write(f"{building_url}\n")
