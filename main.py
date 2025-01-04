import requests
from bs4 import BeautifulSoup

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
    textes=[]
    for row in rows :
        colonnes = row.find_all('td')
        texte_annonce=colonnes[7].get_text().strip()
        textes.append(texte_annonce)
    print(*textes, sep='\n')
else:
    print(f"Erreur : Code HTTP {response.status_code}")