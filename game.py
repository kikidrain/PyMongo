import random
import time
from models import Entity
from utils import create_character_from_liste, get_all_characters, get_all_monsters, show_entity, get_choice, print_header, print_line, clean_screen


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
    characters = create_character_from_liste(get_all_characters())
    
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
    time.sleep(2.0)


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
    time.sleep(2.0)


def check_combat_end(team, enemies):
    team_alive = any(character.is_alive() for character in team)
    enemies_alive = any(enemy.is_alive() for enemy in enemies)
    
    if not team_alive:
        return True
    elif not enemies_alive:
        return False
    
def start_combat(team, wave_number):
    print_header(f"Vague {wave_number}")
    
    monsters_from_db = get_all_monsters()
    all_monsters = create_character_from_liste(monsters_from_db)
    
    enemies = []
    number_of_enemies = min(wave_number, len(all_monsters))
    
    #faire apparaître ennemis aleatoirement 
    for _ in range(number_of_enemies): 
        monster = random.choice(all_monsters)
        enemies.append(Entity(monster.name, monster.attack, monster.defense, monster.max_health))
    
    print(f"\n{number_of_enemies} ennemis apparaissent")
    for enemy in enemies:
        print(f"- {enemy.name}")

    time.sleep(2.0)
    
    
    while True:
        show_combat_status(team, enemies)
        player_turn(team, enemies)
        
        # vérifier si le combat est terminé sans victoire ni défaite 
        result = check_combat_end(team, enemies)
        if result is True:
            return True
        
        enemy_turn(team, enemies)
        
        result = check_combat_end(team, enemies)
        if result is True:
            return True
