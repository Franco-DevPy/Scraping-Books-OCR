# Projet de Web Scraping des Livres

Ce projet effectue un scraping du site [Books to Scrape](https://books.toscrape.com/) pour extraire des informations sur les catégories et les livres, en sauvegardant les données dans des fichiers CSV, avec le téléchargement des images.

## Description

L'objectif de cette application est d'automatiser la collecte de données du site Books to Scrape. L'application réalise les tâches suivantes :

- Récupère toutes les catégories de livres disponibles.
- Extrait des informations pour chaque livre de chaque catégorie, comme le titre, le prix, le stock, la note, la description et l'URL de l'image.
- Enregistre les informations des livres dans des fichiers CSV, organisés par catégorie.
- Télécharge les images de chaque livre et les enregistre dans un dossier spécifique.

## Installation

### Prérequis

- Python 3.x installé sur votre machine.

### Étapes

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/Franco-DevPy/Scraping-Books-OCR.git
   ```

2. **Aller dans le répertoire du projet**

   ```bash
   cd Scraping-Books-OCR
   ```

3. **Cree un environement virtuel**
   ```bash
   python -m venv venv
   ```

4. **Activer l'environement**
   # Windows
   ```bash
   .\venv\Scripts\activate
   ```
   # Linux
   ```bash
   source env/bin/activate
   ```
   # Quitter l'environement

   ```bash
   # Windows and Linux
   deactivate
   ```
   
   
5. **Installer les dépendances**
   ```bash
    pip install -r requirements.txt
   ```


6. **Pour exécuter le script principal et lancer le scraping, utilisez la commande suivante :**
   ```bash
    py main.py
   ```




Le script extraira les informations des livres et les enregistrera dans des fichiers CSV sous le répertoire scraping/data/csv/. Les images des livres seront téléchargées dans le répertoire scraping/data/img/.



### Structure du Projet

main.py : Script principal qui lance le scraping pour toutes les catégories.
scraping/categories.py : Contient les fonctions pour récupérer les URL des catégories et les livres de chaque catégorie.
scraping/singlebook.py : Contient les fonctions pour extraire les informations spécifiques à chaque livre.
scraping/data/csv/ : Dossier où seront stockés les fichiers CSV générés.
scraping/data/img/ : Dossier où seront stockées les images téléchargées.


