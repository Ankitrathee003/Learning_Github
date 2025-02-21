import requests
from bs4 import BeautifulSoup


url = 'https://soax.com/scraping/ecommerce'

# response = requests.get(url)

def fetchAndSaveToFile(url, path):
    r = requests.get(url)  # Makes an HTTP GET request to the provided URL
    with open(path, "w") as f:  # Opens the specified file path in write mode
        f.write(r.text)  # Writes the response text (HTML, JSON, etc.) to the file

soup=BeautifulSoup()
fetchAndSaveToFile(url,"Inspect_file_2.html")
# print("completed")

with open("Inspect_file_2.html", "r") as f:
    html_file=f.read()

# ulTag = soup.new_tag("ul")
# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "About"
# ulTag.append(liTag)

# soup.html.body.insert(0, ulTag)

# with open("modified.html", "w") as f:
#     f.write(str(soup))
