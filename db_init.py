
from pymongo import MongoClient

personnages = [
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

monstres = [
    {"name": "Gobelin", "attack": 9, "defense": 5, "health": 50},
    {"name": "Orc", "attack": 19, "defense": 8, "health": 120},
    {"name": "Dragon", "attack": 34, "defense": 20, "health": 300},
    {"name": "Zombie", "attack": 11, "defense": 6, "health": 70},
    {"name": "Troll", "attack": 24, "defense": 15, "health": 200},
    {"name": "Spectre", "attack": 17, "defense": 10, "health": 100},
    {"name": "Golem", "attack": 25, "defense": 28, "health": 250},
    {"name": "Vampire", "attack": 21, "defense": 12, "health": 150},
    {"name": "Loup-garou", "attack": 27, "defense": 16, "health": 180},
    {"name": "Squelette", "attack": 14, "defense": 7, "health": 75}
]


def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client["test_jeu"]

    db["personnages"].delete_many({})
    db["monstres"].delete_many({})
    db["scores"].delete_many({})

    db["personnages"].insert_many(personnages)
    db["monstres"].insert_many(monstres)

    db["scores"].create_index([("score", -1)])

    nb_perso = db["personnages"].count_documents({})
    nb_monstres = db["monstres"].count_documents({})

    print("Initialisation terminée.")
    print(f"{nb_perso} personnages insérés")
    print(f"{nb_monstres} monstres insérés")


if __name__ == "__main__":
    main()
