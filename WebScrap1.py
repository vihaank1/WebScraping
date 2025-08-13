import requests  # For sending HTTP requests to websites
from bs4 import BeautifulSoup  # For parsing and extracting data from HTML

# Get the HTML content from the website
web = requests.get("https://www.tutorialsfreak.com/")
print(web)  # Print response object info

print(web.url)  # Print the actual URL fetched
print(web.status_code)  # Print status code (200 means OK)

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(web.content, "html.parser")
print(soup.prettify())  # Print nicely formatted HTML

print(soup.title)  # Print the <title> tag of the page
print("--------")

print(soup.find_all("p"))  # Find and print all <p> (paragraph) tags

tag = soup.html  # Get the <html> tag
print(type(tag))  # Print type of the tag object
print("")

tags = soup.h1  # Get the first <h1> tag
print(tags)
print("")

super = soup.h2  # Get the first <h2> tag
print(super)

create = soup.p.string  # Get the text inside the first <p> tag
print(create)
print("")

# Find first <div> with class "app-container"
class_info = soup.find("div", class_="app-container")
print(class_info)
print("")

# Find first <div> with id "app-container"
id_data = soup.find("div", id="app-container")
if id_data:  # Check if element exists before using it
    print(id_data.find_all("a"))  # Print all <a> tags inside it
else:
    print("No element found with id='app-container'")

# Find all <img> tags and print their "src" attribute
img = soup.find_all("img")
for i in img:
    print(i.get("src"))

print("")

# Print the "alt" text for each <img> tag
for i in img:
    print(i.get("alt"))
