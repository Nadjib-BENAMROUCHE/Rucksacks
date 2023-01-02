# -*- coding: utf-8 -*-
from venv import create
import psycopg2
import datetime
import gzip 
import sys

# Recuperation des donnée 
def Get_data(input_file) :

    # ouverture du fichier en mode lecture
    my_file = open(input_file, "r")

    # lecture du fichier
    data = my_file.read()

    # diviser le texte pour construire une liste 
    rucksacks = data.split("\n")

    # fermer le fichier
    my_file.close()

    return rucksacks



# Fonction pour chercher et trouver les erreurs 
def Find_errors(rucksacks):
    # créer une liste pour les erreurs 
    errors = []
    # parcourir les sacs 
    for rucksack in rucksacks:
        # diviser la liste de caractère en deux partie pour les compartiments   
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]

        # compter le nombre d'occurrences de chaque élément
        first_counts = {}
        second_counts = {}

        # vérifier si un seul type d'élément apparaît dans les deux compartiments
        for c in first_compartment:
            if c in first_counts:
                first_counts[c] += 1
            else:
                first_counts[c] = 1
        for c in second_compartment:
            if c in second_counts:
                second_counts[c] += 1
            else:
                second_counts[c] = 1
        for c in first_counts:
            # si le caractère existe dans le premier compartiment et le deuxième on l'ajoute dans la liste des erreurs 
            if c in second_counts:
                errors.append(c)

    return errors

# Fonction pour calculer les priorités des objets qui possant le probleme
def Get_scores(liste_errors):
    liste_score = []
    for i in range(len(liste_errors)):
        item = liste_errors[i]
        # les types d'éléments en minuscules de a à z ont des priorités de 1 à 26
        if 'a' <= item <= 'z':
            # la fonction ord pour renvoie le code Unicode de caractère 
            score = ord(item) - ord('a') + 1

        # les types d'éléments en majuscules A à Z ont des priorités de 27 à 52.
        else:
            score = ord(item) - ord('A') + 27
         
        liste_score.append(score)

    return liste_score

# La somme des priorite et le score final 
def Somme(liste):
    # pour calculer la somme des objets ranger incorrectement 
    sum = 0
    for i in range(len(liste)):
        sum += liste[i]

    return sum

# Function pour créer la table rucksacks dans la base de données postgres
def  Create_table():
    # Connexion à la base de données
    conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='1234')

    # Creation de table rucksacks
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE rucksacks (execution_time TIMESTAMP, input_file VARCHAR(255), resultat VARCHAR(255))")    
    conn.commit()

    conn.close()


# Fonction permettant de compresser le fichier d'entrée et d'insérer les données dans la base de données
def Compress_and_insert(input_file):
    # Connexion à la base de données
    conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='1234')

    # Compression du fichier d'entrée
    with open(input_file, 'rb') as f_in:    
        with gzip.open('input.txt.gz', 'wb') as f_out:
            f_out.writelines(f_in)

    # Insertion des données dans la base de données
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rucksacks (execution_time, input_file, resultat) VALUES (%s, %s, %s)", (datetime.datetime.now(), 'inputfile.txt.gz', resultat))
    conn.commit()

    # Fermeture de la connexion à la base de données
    conn.close()


if __name__ == "__main__":
    input_file = sys.argv[1] 
    rucksacks = Get_data(input_file)
    # la liste des erreurs
    errors = Find_errors(rucksacks)
    print(errors)
    # la liste des scores de chaque item 
    scores = Get_scores(errors)
    print(scores)
    # la somme des scores
    resultat = Somme(scores)
    print("La somme finale des objets à réorganiser :",resultat)
    #Create_table()
    Compress_and_insert(input_file) 
    