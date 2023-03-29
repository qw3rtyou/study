import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

# URL of the webpage to crawl
url = "https://bsaber.com/"

# Parse the URL to get the base URL
base_url = url.split('/')[0] + '//' + url.split('/')[2]

# Check the robots.txt file to see if crawling is allowed
robot_parser = RobotFileParser()
robot_parser.set_url(base_url + '/robots.txt')
robot_parser.read()
if not robot_parser.can_fetch('*', url):
    print('Crawling not allowed for this URL')
    exit()

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        links.append(href)

# Print the list of links
print(links)