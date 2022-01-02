# Dashboard Rapport
------------------------------------------

## Description du sujet 
-----------------------

Nous avons décidé que mener ce projet sur l'effecrtif médical dans les différents départements français, c'est un sujet intérressant encore plus en ces temps de crise sanitaire ou l'on a pu observer des disparités importante face à l'épidemie.

  Un aperçu des jeux de données utilisé :  
  
    La première servant à la carte témoin (carte 1)   
    La seconde servant à notre sujet (carte 2)    
    
  Les cartes :  
    La carte témoin (carte 1) représentant par des petit carrés le centre de chaque département français, lors du survol d'un point à l'aide de la soiris, les coordonnées, le nom du départment et son nombre d'habitant apparait.`  
      
    La carte montrant l'effectif (carte 2) représentant par des petit cercles, le centre de chaque département français, lors du survol d'un point à l'aide de la soiris, les coordonnées, le nom du départment et son nombre de médecin exerçant dans ce départment.`  
    
    
## User Guide
-----------------------

__PREREQUIS__ :   

1.Télécharger le fichier compressé sur votre machine (en local) , décompressez-le et placer le dans un autre répertoire au besoin.  
2.Ouvrez un terminal de commandes afin entrer les commandes nécessaires a l'execution du fichier  : 

●	pip install dash  

●	pip install plotly  

●	pip install pandas  

●	pip install numpy  

●	pip install dash

●	pip install matplotlib

3.Placer vous à l'endroit ou vous avez placer le dossier télécharger précédement.  
4.Taper la commande suivant : > python dashboard.py   
5.Ouvrez votre navigateur et aller à l'adresse suivante : > http://127.0.0.1:8050/  


## Developper Guide
-----------------------


Le projet contient en tout 3 fichiers : Le fichier python que l'on doit lancer dans le terminal et les 2 jeux de données

Le fichier dashboard.py est séparé en 3 parties principale :  
  
  Des imports, l'ouverture et le stockage des deux fichiers csv.      
  La creation des différentes figures  
  La création du layout de l'application dash permettant l'affichange de nos figure sur une page html structurée.  
  
  
 ---------
 ###### (Maxine LAMA & Valentin DUMAS)
