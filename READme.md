Jeu de Combat au Tour par Tour

Description : 

Jeu de combat au tour par tour en Python. Le joueur constitue une équipe de 3 personnages et affronte des vagues d'ennemis successives. L'objectif est de survivre au maximum de vagues possible.

Fonctionnalités :

Sélection d'une équipe de 3 personnages parmi 10 personnages disponibles
Système de combat automatique en tour par tour
Progression par vagues d'ennemis
Calcul des dégâts avec réduction basée sur la défense en %
Sauvegarde des scores et classement des meilleurs joueurs
Interface en ligne de commande


Installation

1. Cloner le dépôt :
git clone https://github.com/kikidrain/PyMongo

2 Initialiser la base de données 
python db_init.py


Utilisation

Lancer le jeu avec la commande :

python main.py


Menu principal

Le jeu propose 3 options :

Démarrer une nouvelle partie
Afficher le classement des meilleurs scores
Quitter le jeu

Déroulement d'une partie

Saisir un pseudo
Choisir 3 personnages pour constituer votre équipe
Affronter les vagues d'ennemis successives
La partie se termine lorsque tous les personnages de l'équipe sont éliminés
Le score final correspond au nombre de vagues surmontées

Structure du projet

main.py : Point d'entrée du jeu, gestion du menu et de la boucle principale
game.py : Logique de combat, création d'équipe et gestion des vagues
models.py : Définition de la classe Entity 
utils.py : Fonctions utilitaires 
db_init.py : Script d'initialisation de la base de données


Calcul des dégâts

Réduction = Défense × 0.15
Dégâts réels = max(1, Attaque - Réduction)

Déroulement d'un tour

Tour du joueur : chaque personnage vivant attaque un ennemi aléatoire
Tour de l'ennemi : chaque ennemi vivant attaque un personnage aléatoire
Vérification de fin de combat (tous les ennemis ou tous les personnages éliminés)

Base de données

Le jeu utilise MongoDB avec la base `jeu_tpt` contenant 3 collections :
characters : Liste des personnages jouables
monsters : Liste des monstres
scores : Classement des joueurs 
