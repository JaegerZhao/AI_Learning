# import requests
# from bs4 import BeautifulSoup

# # URL of the webpage to scrape
# url = "https://www.dpm.org.cn/explore/buildings.html"

# # Send a GET request to the webpage
# response = requests.get(url)

# # Parse the HTML content of the page using BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all building links
# building_links = soup.find_all('a', href=True)

# # Filter out links that do not contain '/explore/building/'
# building_links = [link for link in building_links if '/explore/building/' in link['href']]

# # Open a file to write the building names and URLs
# with open('building_links.txt', 'w', encoding='utf-8') as file:
#     # Format and write the building names and URLs to the file
#     for link in building_links:
#         building_name = link.text.strip()
#         building_url = f"https://www.dpm.org.cn{link['href']}"
#         file.write(f"{building_url}\n")

import requests
from bs4 import BeautifulSoup

# Function to get building links from a single page
def get_building_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    building_links = soup.find_all('a', href=True)
    return [link for link in building_links if '/explore/building/' in link['href']]

# Function to write building links to a file
def write_links_to_file(links, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for link in links:
            building_name = link.text.strip()
            building_url = f"https://www.dpm.org.cn{link['href']}"
            file.write(f"{building_url}\n")

# Base URL for pagination
base_url = "https://www.dpm.org.cn/searchs/buildings/category_id/73/sort/sortrank/qj/0/p"

# Start with the first page
page_number = 1

# Maximum number of pages to scrape
max_pages = 12  # Adjust this number based on the actual number of pages

# Loop through pages until the maximum page number is reached
for page_number in range(1, max_pages + 1):
    # Construct the URL for the current page
    page_url = f"{base_url}/{page_number}.html"
    
    # Get building links from the current page
    links = get_building_links(page_url)
    
    # Write the links to the file
    write_links_to_file(links, 'building_links.txt')

# Print a success message
print("All building links have been successfully saved to building_links.txt")
