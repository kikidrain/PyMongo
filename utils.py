import os
from pymongo import MongoClient
from models import Entity


def get_database():
    client = MongoClient('mongodb://localhost:27017/')
    return client["jeu_tpt"]

def print_line(size=35):
    print("─"*size)

def print_header(message):
    print("\n")
    print_line()
    print(f"\t\t{message}")
    print_line()

# récuperer les entités de la db
def get_all_characters():
    db = get_database()
    return list(db["characters"].find({}))

def create_character_from_liste(liste_character_from_db):
    # creer une liste de character a partir du retour de la db
    characters = []
    for char_db in liste_character_from_db:
        character = Entity(char_db["name"],char_db["attack"],char_db["defense"],char_db["health"])
        characters.append(character)
        
    return characters

def get_all_monsters():
    db = get_database()
    return list(db["monsters"].find({}))

#on verra plus tard 
def get_monsters_by_clan(clan_name):
    db = get_database()
    return list(db["monsters"].find({"clan": clan_name}))

#afficher les stats 
def show_entity(entity, index):
    print(f"{index}. {entity.name} - {entity.attack} ATK - {entity.defense} DEF - {entity.health} HEALTH")

#save les scores 
def save_score(player_name, score):
    db = get_database()
    db["scores"].insert_one({"player_name": player_name, "score": score})


def get_choice(message, valid_choices):

    while True:
        choice = input(message).strip()
        if choice in valid_choices:
            return choice
        else:
            print("pas la bonne option")


def get_player_name():

    while True:
        player_name = input("\nChoisi ton pseudo -> ").strip()
        if player_name:
            return player_name
        else:
            print("Le pseudo doit contenir au moins 1 caractère")