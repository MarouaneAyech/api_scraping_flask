import requests
from bs4 import BeautifulSoup
import json

# URL cible
url = "http://www.tunisie-annonce.com/AnnoncesImmobilier.asp"
# Envoyer une requête GET à la page
response = requests.get(url)
# Vérifier si la requête est réussie
if response.status_code == 200:
    # Parser le contenu HTML de la page
    soup = BeautifulSoup(response.content, 'html.parser')
    # Trouver la table contenant les annonces
    rows = soup.find_all('tr', class_='Tableau1')
    annonces=[]
    for row in rows :
        annonce={}
        colonnes = row.find_all('td')
        annonce['texte'] = colonnes[7].get_text().strip()
        annonce['nature'] = colonnes[3].get_text().strip()
        annonce['prix'] = colonnes[9].get_text().strip()
        annonces.append(annonce)
    with open('annonces.json','w') as file :
            json.dump(annonces, file)
else:
    print(f"Erreur : Code HTTP {response.status_code}")