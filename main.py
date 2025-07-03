from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController

if __name__ == "__main__":
    # Ajouter des joueurs
    pc = PlayerController()
    pc.add_player()
    # pc.add_player()

    # Créer un tournoi
    tc = TournamentController()
    # tc.create_tournament()

    # Afficher les joueurs
    # pc.show_all_players()

    # Lancer le tournoi
    # tc.start_tournament()
