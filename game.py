import random
from models import Entity
from utils import create_character_from_liste, get_all_characters, get_all_monsters, show_entity, get_choice, print_header, print_line


def show_team(team):
    print_header("Voici votre équipe actuelle")
    if not team:
        print("\nl'équipe est vide choisi 3 perso")
    else:
        for index, character in enumerate(team):
            print(f"{index+1} {character}")
    print_line()


def create_team():
    team = []
    all_characters = get_all_characters()
    # pour pouvoir selectionner les personnage qui n'ont impérativement pas de clan et pas avoir de perso broken dans l'équipe
    available_characters = [c for c in all_characters if c.get("clan") is None]
    characters = create_character_from_liste(available_characters)
    
    print_header("Choisis 3 perso pour ton équipe")
    for index, character in enumerate(characters):
        show_entity(character, index+1)
    print_line()

    while len(team) < 3:
        valid_choices = []
        for i in range(1, len(characters)+1):
            valid_choices.append(str(i))
        
        choice = get_choice(f"\nChoisis le personnage {len(team)+1} (1-{len(characters)}) : ", valid_choices)
        selected_character = characters[int(choice)-1]
        
        if selected_character in team:
            print("\nTu as déjà choisi ce perso choisi un autre")
        else:
            team.append(selected_character)
            print(f"\n{selected_character.name} a été ajouté à l'équipe")
  
    show_team(team)
    return team


def show_combat_status(team, enemies):
    print("\n")
    print_line()
    print("VOTRE EQUIPE:")
    for index, character in enumerate(team):
        if character.is_alive():
            print(f"{index+1}. {character.name} - HP: {character.health}/{character.max_health}")
        else:
            print(f"{index+1}. {character.name} - MORT")
    print("\nENNEMI:")
    for index, enemy in enumerate(enemies):
        if enemy.is_alive():
            print(f"{index+1}. {enemy.name} - HP: {enemy.health}/{enemy.max_health}")
        else:
            print(f"{index+1}. {enemy.name} - MORT")
    print_line()


def player_turn(team, enemies):
    print_header("Votre tour")
    alive_enemies = []
    for enemy in enemies:
        if enemy.is_alive():
            alive_enemies.append(enemy)
    
    for character in team:
        if character.is_alive() and len(alive_enemies) > 0:
            target = random.choice(alive_enemies)
            damage = character.attack_target(target)
            print(f"\n{character.name} inflige {damage} dégats à {target.name}")
            if not target.is_alive():
                print(f"{target.name} est mort")
                alive_enemies.remove(target)
    input("\n Appuyez Entrée pour continuer")


def enemy_turn(team, enemies):
    print_header("Tour ennemi")
    alive_characters = []
    for character in team:
        if character.is_alive():
            alive_characters.append(character)
    
    for enemy in enemies:
        if enemy.is_alive() and len(alive_characters) > 0:
            target = random.choice(alive_characters)
            damage = enemy.attack_target(target)
            print(f"\n{enemy.name} inflige {damage} dégats à {target.name}")
            if not target.is_alive():
                print(f"{target.name} est mort")
                alive_characters.remove(target)
    input("\nAppuyez Entrée pour continuer")


def check_combat_end(team, enemies):
    team_alive = any(character.is_alive() for character in team)
    enemies_alive = any(enemy.is_alive() for enemy in enemies)
    
    if not team_alive:
        return True
    elif not enemies_alive:
        return False
    
def start_combat(team, wave_number):
    print_header(f"Vague {wave_number}")
    
    from utils import get_all_characters
    
    all_characters = get_all_characters()
    monsters_from_db = get_all_monsters()
    
    # pour split les monstres normaux des clans 
    normal_monsters = [m for m in monsters_from_db if m.get("clan") not in ["BravM", "Vamp", "Troupe du Faucon", "Hunter"]]
    brav_m_monsters = [m for m in monsters_from_db if m.get("clan") == "BravM"]
    alucard_monster = [m for m in monsters_from_db if m.get("name") == "Alucard"]
    griffith_monster = [m for m in monsters_from_db if m.get("name") == "Griffith"]
    anderson_char = [c for c in all_characters if c.get("name") == "Anderson"]
    guts_char = [c for c in all_characters if c.get("name") == "Guts"]
    silva_char = [c for c in all_characters if c.get("name") == "Silva"]
    chrollo_monster = [m for m in monsters_from_db if m.get("name") == "Chrollo"]
    
    normal_monsters_entities = create_character_from_liste(normal_monsters)
    brav_m_entities = create_character_from_liste(brav_m_monsters)
    
    enemies = []
    number_of_enemies = min(wave_number, len(normal_monsters))
    
    #faire apparaitre ennemis aleatoire
    available_monsters = normal_monsters_entities.copy()
    for _ in range(number_of_enemies): 
        monster = random.choice(available_monsters)
        enemies.append(Entity(monster.name, monster.attack, monster.defense, monster.max_health))
        available_monsters.remove(monster)
    
    # 1 chance sur 7 qu'un membre de la BravM apparaisse
    brav_member_name = None
    if random.randint(1, 7) == 1 and brav_m_entities:
        brav_monster = random.choice(brav_m_entities)
        brav_member_name = brav_monster.name
        enemies.append(Entity(brav_monster.name, brav_monster.attack, brav_monster.defense, brav_monster.max_health))
    
    # 1 chance sur 10 que Anderson et Alucard apparaissent
    anderson_appears = False
    alucard_appears = False
    if random.randint(1, 10) == 1:
        if anderson_char:
            anderson_data = anderson_char[0]
            team.append(Entity(anderson_data["name"], anderson_data["attack"], anderson_data["defense"], anderson_data["health"]))
            anderson_appears = True
        if alucard_monster:
            alucard_data = alucard_monster[0]
            enemies.append(Entity(alucard_data["name"], alucard_data["attack"], alucard_data["defense"], alucard_data["health"]))
            alucard_appears = True
    
    # 1 chance sur 10 que Guts et Griffith apparaissent
    guts_appears = False
    griffith_appears = False
    if random.randint(1, 10) == 1:
        if guts_char:
            guts_data = guts_char[0]
            team.append(Entity(guts_data["name"], guts_data["attack"], guts_data["defense"], guts_data["health"]))
            guts_appears = True
        if griffith_monster:
            griffith_data = griffith_monster[0]
            enemies.append(Entity(griffith_data["name"], griffith_data["attack"], griffith_data["defense"], griffith_data["health"]))
            griffith_appears = True

    # 1 chance sur 10 que Silva et Chrollo apparaissent
    silva_appears = False
    chrollo_appears = False
    if random.randint(1, 10) == 1:
        if silva_char:
            silva_data = silva_char[0]
            team.append(Entity(silva_data["name"], silva_data["attack"], silva_data["defense"], silva_data["health"]))
            silva_appears = True
        if chrollo_monster:
            chrollo_data = chrollo_monster[0]
            enemies.append(Entity(chrollo_data["name"], chrollo_data["attack"], chrollo_data["defense"], chrollo_data["health"]))
            chrollo_appears = True

    print(f"\n{len(enemies)} ennemis apparaissent")
    for enemy in enemies:
        print(f"- {enemy.name}")
    
    if brav_member_name:
        print(f"\n [{brav_member_name}] de la BravM est apparu !")
    
    if anderson_appears and alucard_appears:
        print("\n Anderson et Alucard font leur entrée !")
    
    if guts_appears and griffith_appears:
        print("\n Guts et Griffith font leur entrée !")

    if silva_appears and chrollo_appears:
        print("\n Silva et Chrollo font leur entrée !")
    input("\nAppuyez Entrée pour continuer")
    
    
    while True:
        show_combat_status(team, enemies)
        player_turn(team, enemies)
        
        # pour verifier si le tour est terminer
        result = check_combat_end(team, enemies)
        if result is not None:
            return result
        
        enemy_turn(team, enemies)
        
        result = check_combat_end(team, enemies)
        if result is not None:
            return result