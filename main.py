import requests
from bs4 import BeautifulSoup
import json

from flask import Flask, jsonify

app = Flask(__name__)

# URL cible
url = "http://www.tunisie-annonce.com/AnnoncesImmobilier.asp"

@app.route('/scrape', methods=['GET'])
def scrape_annonces():
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
        return jsonify(annonces)
    else:
        return jsonify({"error": f"Erreur : Code HTTP {response.status_code}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
