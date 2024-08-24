# Projet de Web Scraping des Livres

Ce projet effectue un scraping du site [Books to Scrape](https://books.toscrape.com/) pour extraire des informations sur les catégories et les livres, en sauvegardant les données dans des fichiers CSV, avec le téléchargement des images.


## Description

L'objectif de cette application est d'automatiser la collecte de données du site Books to Scrape. 
L'application réalise les tâches suivantes :

- Récupère toutes les catégories de livres disponibles.
- Extrait des informations pour chaque livre de chaque catégorie, comme le titre, le prix, le stock, la note,
 la description et l'URL de l'image.
- Enregistre les informations des livres dans des fichiers CSV, organisés par catégorie.
- Télécharge les images de chaque livre et les enregistre dans un dossier spécifique.

## Installation

Pour exécuter ce projet sur votre machine locale, suivez ces étapes :

```bash
# Cloner le dépôt
git clone https://github.com/Franco-DevPy/scrapTRY.git

# Aller dans le répertoire du projet
cd nom-du-projet

# Installer les dépendances
pip install -r requirements.txt
