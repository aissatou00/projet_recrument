# Projet Django REST : Recrutement API 

# Objectif du projet :
Exposer une API REST pour une plateforme de recrutement avec deux profils : Candidat et Recruteur.


# Fonctionnalités demandées :
Un ou plusieurs modèles liés à une base de données PostgreSQL
Des endpoints API pour les candidats : création et consultation de profil
Des endpoints API pour les recruteurs : possibilité de lister les candidats
Documentation interactive de l'API avec Swagger (drf-yasg)



#  Technologies
- Python 3.10+
- Django 4+
- Django REST Framework
- PostgreSQL
- Swagger (drf-yasg)


#  Installation & exécution

# 1. Cloner le projet
git clone  https://github.com/aissatou00/projet_recrument.git

cd recrutement_api

# 2. Création et activation de l'environnement virtuel
python -m venv env
source env/bin/activate  ou sur Windows :  source env\Scripts\activate

# 3. Installation des dépendances
- Créer un fichier `requirements.txt` contenant :
Django>=4.0
djangorestframework
psycopg2-binary
drf-yasg

- Installer les dépendances avec la commande:
pip install -r requirements.txt


# 4. Configuration PostgreSQL dans le fichier backend/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recrutement_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# 5. Créeation de la base de données PostgreSQL
- Taper la commande :
psql -U postgres
CREATE DATABASE recrutement_db;


# 6. Lancement du projet 
- Application des migrations et démarrage du serveur local :
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  
python manage.py runserver


# Création d'un Recruteur et utilisation de son ID pour créer des Candidats

- Ouvrons la console Django avec cette commande :
python manage.py shell

-  création d'un Recruteur :
from api.models import Recruteur
recruteur = Recruteur.objects.create(
    nom="Vegba", 
    entreprise="Lux",
    email="Vegba@test.com"
)


# Accès aux interfaces
- API Swagger : [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Django Admin : [http://localhost:8000/admin/](http://localhost:8000/admin/)



# Diagramme UML
- Diagramme UML des modèles Candidat et Recruteur montrant les relations
disponible dans le dossier uml_recrutement


# Commandes Git
git init
git remote add origin https://github.com/aissatou00/projet_recrument.git
git add .
git commit -m "Initial commit"
git push -u origin main



#  Ressources utiles
- [DRF Documentation](https://www.django-rest-framework.org/)
- [DRF Swagger](https://www.django-rest-framework.org/topics/documenting-your-api/)
- [Tuto Django + DRF](https://www.youtube.com/watch?v=JC6gHKeegk4)



