import requests
from bs4 import BeautifulSoup

city = input("Enter the City Name: ") 
search = "Weather in {}".format(city) 
  
url = f"https://www.google.com/jsearch?&q ={search}" 

req = requests.get(url) 
 
sor = BeautifulSoup(req.text, "html.parser")  

temp = sor.find("div", class_='default')
print(temp) 

