from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

def main():
    pc = PlayerController()
    tc = TournamentController()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Ajouter un joueur")
        print("2 - Voir tous les joueurs")
        print("3 - Créer un tournoi")
        print("4 - Voir tous les tournois")
        print("5 - Lancer un tournoi")
        print("6 - Afficher les rapports (à venir)")
        print("0 - Quitter")

        choice = input("Votre choix : ").strip()

        if choice == "1":
            pc.add_player()
        elif choice == "2":
            pc.show_all_players()
        elif choice == "3":
            tc.create_tournament()
        elif choice == "4":
            tc.show_all_tournaments()
        elif choice == "5":
            tc.start_tournament()
        elif choice == "6":
            print("🔧 Fonctionnalité à venir.")
        elif choice == "0":
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
