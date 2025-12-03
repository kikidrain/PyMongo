from pymongo import MongoClient

def get_database():
    client = MongoClient('mongodb://localhost:27017/')
    return client["jeu_tpt"]

# Récupérer les entités
def get_all_characters():
    db = get_database()
    return list(db["characters"].find({}))

def get_all_monsters():
    db = get_database()
    return list(db["monsters"].find({}))

#on verra plus tard 
def get_monsters_by_clan(clan_name):
    db = get_database()
    return list(db["monsters"].find({"clan": clan_name}))

#afficher les stats 
def show_entity(entity, index):
    print(f"{index}. {entity['name']} - {entity['attack']} ATK - {entity['defense']} DEF - {entity['health']} HEALTH")

#save les scores 
def save_score(player_name, score):
    db = get_database()
    db["scores"].insert_one({"player_name": player_name, "score": score})


def get_choice(message, valid_choices):
    #la personne entre la chaise et son écran fait un choix
    while True:
        choice = input(message).strip()
        if choice in valid_choices:
            return choice
        else:
            print("pas la bonne option")


def get_player_name():
    #choisir le nom du joueur
    while True:
        player_name = input("\nChoisi ton pseudo ").strip()
        if player_name:
            return player_name
        else:
            print("Le pseudo doit contenir au moins 1 caractère")
