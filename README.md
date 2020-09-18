# Pybot

## Introduction

Cette application web permet de récupérer des informations et / ou l'adresse de différentes reqûetes émises par un utilisateur.

Adresse du site en production: 

https://pybot-scrapper.herokuapp.com/


--------------------------

## Utilisation

1. Poser une question à Pybot : celui ci parsera la question à la recherche des mots adresse et information. 
2. Dépendant de ces mots il va requêter différentes api (Google maps API et Wikimedia API)
3. Dépéndant de ces mots il va afficher l'addresse et ou des informations sur le lieu demandé.
4. Il affichera également un "pin" sur la carte à l'endroit associé à la reqûete.

-------------------

## Contribution

##### Forkez le repository disponible à l'adresse suivante: [Pybot - Github](https://github.com/MaewenPell/pybot.git)
##### Le projet est organisé en différents dossiers:
- actions : Python file utilisés pour envoyer des requêtes aux API, et effectuer le parsing de la reqûete envoyée par l'utilisateur.
- static/ : Imgs/ et Style/ dossiers contenant la fiche CSS et différentes images utilisés
- static/ : js/ javascript file utilisé pour faire remonté la requête AJAX de l'utilisateur et la transmettre au fichiers Python pour le parsing et afficher une réponse.
- template/ : Fichier HTML pour l'architecture de la page
- test/ : tests unitaires et mock utilisés pour réaliser l'application web

###### Une fois les modifications apportés vous pourrez effectuer une Pull Request et ainsi nous pourrons discuter des modifications que vous souhaitez apporter et pourquoi pas les ajouter en production !

##### Pour lancer le projet en local:

1. Créer une variable MAPS_API_KEY dans le fichier (config.py)
2. Ajouter votre clé API que vous aurez généré via la console google cloud
3. Lancer python run.py à la racine du projet

---------- 
## Fonctionnement général

L'aspect visuel du site est généré par le fichier HTML, et la fiche de style CSS. Lorsqu'un utilisateur entre une reqûete dans le formulaire celle ci va être traitée de cette façon:

1. La reqûete va être traitée en AJAX par le biais de la variable request:
```javascript
query = $('input:text').val();
```

2. Cette requête va être récupérée au niveau des vues (views.py)
```python
query = escape(request.get_data(as_text=True))
```

3. Nous parsons cette réponse pour savoir si l'utilisateur veux des informations / la localisation ou les deux. Nous avons également le lieu demandé.

```python
filtered_query, ad_wanted, info_wanted = parser.filter_words(str(query))
```

4. Nous récupérons la localisation de la demande grace à une requête à l'API de google maps:
```python
lat, lng, _, address = api_requester.get_geocode(filtered_query)
```

5. Nous récupérons des informations sur le lieu grâce à une requête à l'API wikicommons
```python
informations = api_requester.get_data_wiki(filtered_query)
```

6. Enfin nous renvoyons les informations récupérés grace à la fonction Flask jsonify() sous forme de JSON :
```python
return jsonify(query, informations,
               lat, lng, address,
               ad_wanted, info_wanted)
```

7. Cette réponse des vues est mis en forme selon les différents éléments voulus et ré-émis à l'utilisateur grace aux différentes fonctions :

```javascript
user_asking(...)
bot_reply(...)
update_map(...)
```

---------- 
## Tests

Des tests unitaires ainsi que des mocks pour les API ont été mis en place et
ils peuvent être lancés à la racine par le biais de la commande suivante :

```bash
pytest
```

--------
## Ressources utilisés

[Python 3](https://www.python.org/)
[Flask](https://flask.palletsprojects.com/en/1.1.x/)
[Jquery](https://jquery.com/)
[Bootstrap](https://getbootstrap.com/)
[Google Maps](https://developers.google.com/maps/documentation/urls/get-started?hl=fr)
[Media commons](https://www.mediawiki.org/wiki/API:Main_page)

------------------

## Crédits

[Maewen PELLETIER (GitHub)](https://github.com/MaewenPell)
[LinkedIn](https://www.linkedin.com/in/maewen-pelletier/)


