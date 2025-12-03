
from pymongo import MongoClient

characters = [
    {"name": "Guerrier", "attack": 16, "defense": 13, "health": 105},
    {"name": "Mage", "attack": 21, "defense": 7, "health": 85},
    {"name": "Archer", "attack": 20, "defense": 8, "health": 95},
    {"name": "Voleur", "attack": 22, "defense": 9, "health": 90},
    {"name": "Paladin", "attack": 14, "defense": 13, "health": 115},
    {"name": "Sorcier", "attack": 25, "defense": 4, "health": 75},
    {"name": "Chevalier", "attack": 17, "defense": 15, "health": 125},
    {"name": "Moine", "attack": 10, "defense": 17, "health": 105},
    {"name": "Berserker", "attack": 25, "defense": 7, "health": 115},
    {"name": "Chasseur", "attack": 16, "defense": 9, "health": 105}
]

monsters = [
    {"name": "Gobelin", "attack": 9, "defense": 5, "health": 50, "clan": None},
    {"name": "Orc", "attack": 19, "defense": 8, "health": 120, "clan": None},
    {"name": "Dragon", "attack": 34, "defense": 20, "health": 300, "clan": None},
    {"name": "Zombie", "attack": 11, "defense": 6, "health": 70, "clan": None},
    {"name": "Troll", "attack": 24, "defense": 15, "health": 200, "clan": None},
    {"name": "Spectre", "attack": 17, "defense": 10, "health": 100, "clan": None},
    {"name": "Golem", "attack": 25, "defense": 28, "health": 250, "clan": None},
    {"name": "Vampire", "attack": 21, "defense": 12, "health": 150, "clan": None},
    {"name": "Loup-garou", "attack": 27, "defense": 16, "health": 180, "clan": None},
    {"name": "Squelette", "attack": 14, "defense": 7, "health": 75, "clan": None},
    {"name": "André", "attack": 30, "defense": 40, "health": 60, "clan": "BravM"}  #on verra plus tard
]


def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client["jeu_tpt"]

    #supprimer les anciennes donnée
    db["characters"].delete_many({})
    db["monsters"].delete_many({})
    db["scores"].delete_many({})

    #ajuouter les nouveau
    db["characters"].insert_many(characters)
    db["monsters"].insert_many(monsters)

    db["scores"].create_index([("score", -1)])

    nb_characters = db["characters"].count_documents({})
    nb_monsters = db["monsters"].count_documents({})

    print("Initialisation terminé")
    print(f"{nb_characters} personnages insérés")
    print(f"{nb_monsters} monstres insérés")


if __name__ == "__main__":
    main()
