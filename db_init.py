from pymongo import MongoClient

characters = [
    {"name": "Guerrier", "attack": 19, "defense": 15, "health": 115, "clan": None},
    {"name": "Mage", "attack": 24, "defense": 9, "health": 90, "clan": None},
    {"name": "Archer", "attack": 23, "defense": 10, "health": 95, "clan": None},
    {"name": "Voleur", "attack": 25, "defense": 11, "health": 100, "clan": None},
    {"name": "Paladin", "attack": 16, "defense": 16, "health": 125, "clan": None},
    {"name": "Sorcier", "attack": 28, "defense": 6, "health": 80, "clan": None},
    {"name": "Chevalier", "attack": 19, "defense": 18, "health": 135, "clan": None},
    {"name": "Moine", "attack": 12, "defense": 20, "health": 110, "clan": None},
    {"name": "Guts", "attack": 30, "defense": 30, "health": 130, "clan": "Troupe du Faucon"},
    {"name": "Chasseur", "attack": 19, "defense": 11, "health": 110, "clan": None},
    {"name": "Dutch", "attack": 20, "defense": 15, "health": 80, "clan": None},
    {"name": "Anderson", "attack": 22, "defense": 27, "health": 150, "clan": "Vamp"},
    {"name": "Silva", "attack": 40, "defense": 30, "health": 180, "clan": "Hunter"},
]

monsters = [
    {"name": "Gobelin", "attack": 6, "defense": 5, "health": 50, "clan": None},
    {"name": "Orc", "attack": 15, "defense": 8, "health": 120, "clan": None},
    {"name": "Dragon", "attack": 30, "defense": 20, "health": 300, "clan": None},
    {"name": "Zombie", "attack": 8, "defense": 6, "health": 70, "clan": None},
    {"name": "Troll", "attack": 20, "defense": 15, "health": 200, "clan": None},
    {"name": "Spectre", "attack": 14, "defense": 10, "health": 100, "clan": None},
    {"name": "Golem", "attack": 21, "defense": 28, "health": 250, "clan": None},
    {"name": "Loup-garou", "attack": 23, "defense": 16, "health": 180, "clan": None},
    {"name": "Squelette", "attack": 11, "defense": 7, "health": 75, "clan": None},
    {"name": "André", "attack": 18, "defense": 40, "health": 80, "clan": "BravM"},
    {"name": "José", "attack": 35, "defense": 20, "health": 60, "clan": "BravM"},
    {"name": "Vincent", "attack": 25, "defense": 28, "health": 70, "clan": "BravM"},
    {"name": "Alucard", "attack": 30, "defense": 15, "health": 180, "clan": "Vamp"},
    {"name": "Griffith", "attack": 30, "defense": 25, "health": 150, "clan": "Troupe du Faucon"},
    {"name": "Chrollo", "attack": 30, "defense": 40, "health": 170, "clan": "Hunter"},



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