# django

#-Install the Requirements: pip install -r requirements.txt.
#-Then, make database migrations: python3 manage.py makemigrations
#-python3 manage.py migrate
#-And finally, after a successful migration run the application: python3 manage.py runserver
#-At last, open up your favorite web browser
#-Go to URL “http://127.0.0.1/[ PORT_NUMBER ]/“
#-For the Admin Panel credentials, you have to create one with a superuser. 

Le but de ce projet est de créer un site de location/pret de livres avec comme features :
- authentification, pour deux types de profils : libraire et client --OK--
- groupes de lecture, avec plannification de séances (doodle like) --OK--
- gestion des livres (titre, auteur, jaquette, editeur, collection, genre) --OK--
- recherche de livre et de bibliothèque le proposant
- sélection de bibliothèques par zone géographique,
- création/planification des groupes de lectures et adhésion --OK--
- backoffice pour les bibliothèques :
- - ajout de livres --OK--
- - interface de gestion des emprunts --OK--
- - listing des retards de retour de livres 
- - creation de groupes de lectures --OK--
- page d'accueil des patients :
- - rappel des prochains groupes de lectures --OK--
- - rappel des livres à rendre --OK--
- chat/forum
Le site doit être fait avec du Django simple (pas d'API REST, pas de front avec framework type react ou
angular), ignorer cette contrainte conduira à un zero automatiquement.