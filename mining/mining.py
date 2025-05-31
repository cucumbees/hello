import requests
from bs4 import BeautifulSoup

url = "https://www.pokemon.com/us/pokedex"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

nama_heading = soup.find("span",{"id": "pokemon"})

if nama_heading:
    h4 = nama_heading.find_parent("h4")

for sibling in h4.find_next_siblings():
    if sibling.name == "h4":
        break
    if sibling.name == "h5":
        title = sibling.get_text(strip=True)
        print(",",title)
    else:
        print("Nama Pokemon tidak ada")