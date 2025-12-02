from pymongo import MongoClient

def get_database():
    client = MongoClient('mongodb://localhost:27017/')
    return client["encore__un_test"]

# Récupérer les entités
def get_all_characters():
    db = get_database()
    return list(db["characters"].find({}))

def get_all_monsters():
    db = get_database()
    return list(db["monsters"].find({}))

#on verra plus tard 
def get_monsters_by_team(team_name):
    db = get_database()
    return list(db["monsters"].find({"team": team_name}))

#afficher les stats
def display_entity(entity, index):
    print(f"{index}. {entity['name']} - {entity['attack']} ATK - {entity['defense']} DEF - {entity['health']} PV")

