FROM postgres:11
# L'image de base à utiliser est l'image officielle de PostgreSQL version 11

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1234
# Variables d'environnement qui seront utilisées pour configurer l'utilisateur et le mote de passe de l'instance de base de données

EXPOSE 5433
# Indique au conteneur de publier le port 5433 utilisé par PostgreSQL