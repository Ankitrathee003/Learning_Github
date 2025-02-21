# import requests
# from BeautifulSoup4 import BeautifulSoup
# url="https://www.amazon.in/s?k=mobiles+under+20000&ref=nb_sb_noss"
# r=requests.get(url)
# print(r)
# soup=BeautifulSoup(r.text,"lxml")
# print(soup)


import requests
from bs4 import BeautifulSoup

url = 'https://soax.com/scraping/ecommerce'

# Send a GET request to the URL
response = requests.get(url)

## will print HTML file for given URL
# print(response.text)   

def fetchAndSaveToFile(url, path):
    r = requests.get(url)  # Makes an HTTP GET request to the provided URL
    with open(path, "w") as f:  # Opens the specified file path in write mode
        f.write(r.text)  # Writes the response text (HTML, JSON, etc.) to the file


fetchAndSaveToFile(url,"Inspect_file.html")


# soup = BeautifulSoup("html_file", 'html.parser')

with open("Inspect_file.html", "r") as f:
    html_file=f.read()
    

soup = BeautifulSoup(html_file, 'html.parser')  # Making soup object 

# print(type("Inspect_file.html"))    or   print(type(html_file))  ###  <class 'str'>


# for link in soup.find_all("a"):  # All links present in anchor tag will be captured
#       print("printing complete link with text: ",link)
#       print("printing only link: ",link.get("href"))  ## will print only the link     ####printing links:  https://soax.com/research/how-many-people-use-social-media
#       print("printing  text of links: ",link.get_text())


# for link in soup.find_all(id="hs-script-loader"):
#     print("Printing in ID: ",link)

# print(soup.prettify())  ## making it more readable by adding proper indentation and line breaks
                          





# print("printing div tab : ",soup.select("span#hs_cos_wrapper_email_"))  ## when span has id we can refer that id data using # (sapn#ID), will return list 




# for parent in soup.find(id="hs-script-loader").parents:
#     # print("Printing Started")
#     # print("first parent is being printed  ", parent)
#     # print("Printing Finished")
#     break

# cont = soup.find(class_="container")    #soup.find(): This method is used to find the First element that matches the search criteria.
# class_="container"                      #It looks for the first element with the class "container". The underscore (_) after class is necessary because class is a reserved keyword in Python.                                     #The result, cont, will be a tag object representing the first HTML element that has the class "container".
# cont.name = "span"                      # The result, cont, will be a tag object representing the first HTML element that has the class "container".
# cont["class"] = "myclass class2"        #
# cont.string = "I am a string"           #
# print(cont)













# Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find all the titles of articles
#     article_titles = soup.find_all('h2', class_='title')

#     # Print the titles
#     for title in article_titles:
#         print(title.text.strip())
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
