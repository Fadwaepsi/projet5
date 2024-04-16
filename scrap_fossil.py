import requests
from bs4 import BeautifulSoup

url="https://www.fossil.com/fr-fr/montres/montres-pour-femme/"

response = requests.get(url)
#print(response)
content = response.content
#print(content)
soup = BeautifulSoup(content,'html')

prix = soup.findAll('span',class_="value")
print(prix) 
