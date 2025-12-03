import random #pour plus tard 
from models import Entity
from utils import get_all_characters, get_all_monsters, show_entity, get_choice


def show_team(team):
    #affiche la team
    print("\n" + "─"*35)
    print("        Voici votre équipe actuelle")
    print("─"*35)
    
    if not team:
        print("\nl'équipe est vide choisi 3 perso")
    else:
        for i in range(len(team)):
            character = team[i]
            print(f"{i+1} {character}")
    
    print("─"*35)


def create_team():
    team = []
    characters = get_all_characters()
    
    print("\n" + "─"*35)
    print("    Choisis 3 personnages pour ton équipe")
    print("─"*35)
    
    #afficher les perso dispo
    for i in range(len(characters)):
        show_entity(characters[i], i+1)
    print("─"*35)
    
    #le monsieur choisi 3 perso
    while len(team) < 3:
        valid_choices = [str(i+1) for i in range(len(characters))]
        choice = get_choice(f"\nChoisis le personnage {len(team)+1}/3 (1-{len(characters)}): ", valid_choices)

        #voir avec rayan
  
    show_team(team)
    return team