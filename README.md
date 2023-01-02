# Prérequis :
- Python 3.6 ou une version ultérieure
- PostgreSQL 9.6 ou une version ultérieure
- psycopg2 (module Python pour se connecter à PostgreSQL)
- Docker 

# Installation : 
1. Clonez ce dépôt sur votre machine local : git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
2. Accédez au répertoire du projet : cd YOUR_REPO
3. Créez un environnement virtuel Python : python3 -m venv venv
4. Activez l'environnement virtuel : source venv/bin/activate
5. Installez les dépendances du projet : pip install -r requirements.txt

# Configuration : 
- Créez une base de données PostgreSQL et configurez un utilisateur avec les privilèges appropriés : 
database=postgres
user=postgres
password=1234
port=5433
- La base de données postgresql contient une table 'rucksacks' avec trois colonnes : "execution_time", "input_file" et "resultat" 
Vous pouvez aussi creer la table en utilisastion l'appel de la fonction 'Create_table' ligne 126 passer en commantaire dans le fichier 'test.py'

# Exécution :
1. Activez l'environnement virtuel si ce n'est pas déjà fait : 'source venv/bin/activate'
2. Exécutez le script Python pour la verfication des resultats : 'python test.py input.txt' 
Ou bien utiliser le fichier dockerfile pour créer l’image my-test3 et exécuter le script (‘sudo docker build -t my-test3 . ’ puis ‘sudo docker run my-test3’ )
- Executez la commande 'sudo docker-compose up' pour que les deux conteneurs doivent fonctionner simultanément et communiquer entre eux


Nettoyage :
Pour désactiver l'environnement virtuel, utilisez la commande ‘deactivate’.
Pour supprimer l'environnement virtuel, supprimez le répertoire ‘venv’.

#Fichiers fournis :
'test.py' 
'input.txt' 
'dockerfile' : pour le script python
'requirements.txt' : contient les dépendances 
'Dockerfile' : pour la base de données postgresql
'docker-compose.yml' : pour relier le conteneur de la commande et le conteneur pour l'image postgres
