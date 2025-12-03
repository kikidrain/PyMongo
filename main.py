from utils import get_database, get_choice, get_player_name
from game import create_team, show_team


def print_menu():
    #menu principal
    print("\n" + "─"*35)
    print("    Voici le jeu de tout par tour")
    print("─"*35)
    print("\n1 Demarrer le jeu")
    print("2 Afficher le classement")
    print("3 Quitter")
    print("\n" + "─"*35)


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
    #demarrer la partie
    player_name = get_player_name()
    print(f"\nBienvenue {player_name}")
    create_team()

def show_leaderboard():
    db = get_database()
    top_scores = list(db["scores"].find({}).sort("score", -1).limit(3))
    print("\n" + "─"*35)
    print("     Classement des meilleur scores")
    print("─"*35)
    if not top_scores:
        print("\nAucun score de save")
    else:
        for i in range(len(top_scores)):
            score = top_scores[i]
            print(f"{i+1}. {score['player_name']} - {score['score']} vagues")
    print("─"*35)



if __name__ == "__main__":
    main()
