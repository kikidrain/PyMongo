from utils import get_database, get_choice, get_player_name, print_line, print_header, save_score
from game import create_team, show_team, start_combat


def print_menu():
    #menu principal
    print_header("Voici le jeu de tout par tour")

    print("\n1 Demarrer le jeu")
    print("2 Afficher le classement")
    print("3 Quitter")
    print("\n")
    print_line()


def main():
    #boucle d'affiche du menu
    while True:
        print_menu()
        choice = get_choice("Choisissez une option (1-3) ", ['1', '2', '3'])
        
        if choice == '1':
            start_new_game()
        elif choice == '2':
            show_leaderboard()
        elif choice == '3':
            print("\nAurevoir")
            break

def start_new_game():
    player_name = get_player_name()
    print(f"\nBienvenue {player_name}")
    team = create_team()
    wave_number = 1
    
    while True:
        for character in team:
            character.health = character.max_health
        
        team_dead = start_combat(team, wave_number)
        
        if team_dead == True:
            if wave_number > 1:
                final_score = wave_number - 1
                save_score(player_name, final_score)
                print(f"\nScore save vous avez survécu à {final_score} vagues")
            input("\nAppuyer Entrée pour revenir au menu")
            break
        else:
            wave_number = wave_number + 1

def show_leaderboard():
    top_scores = list(get_database()["scores"].find({}).sort("score", -1).limit(3))
    print_header("Classement des meilleur scores")
    
    if not top_scores:
        print("\nAucun score de save")
    else:
        for i, score in enumerate(top_scores):
            print(f"{i+1}. {score['player_name']} - {score['score']} vagues")
    
    print_line()
    input("\nAppuyer Entrée pour revenir au menu")



if __name__ == "__main__":
    main()
