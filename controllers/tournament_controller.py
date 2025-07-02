from models.tournament import Tournament
from models.round import Round
from models.match import Match
from serializers.json_saver import save_data, load_data
from views.tournament_view import TournamentView
from itertools import combinations


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.filename = "data/tournaments.json"
        self.tournaments = self.load_tournaments()

    def load_tournaments(self):
        try:
            return load_data(self.filename, Tournament)
        except FileNotFoundError:
            return []

    def save_tournaments(self):
        save_data(self.tournaments, self.filename)

    def create_tournament(self):
        data = self.view.get_tournament_info()
        tournament = Tournament(**data)
        self.tournaments.append(tournament)
        self.save_tournaments()
        self.view.confirm_save(tournament)

    def show_all_tournaments(self):
        self.view.display_tournaments_list(self.tournaments)

    def resolve_players(self, tournament):
        from controllers.player_controller import PlayerController
        player_lookup = PlayerController().get_players_by_id()

        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                pid1 = match.player1.national_id
                pid2 = match.player2.national_id
                if pid1 in player_lookup:
                    match.player1 = player_lookup[pid1]
                if pid2 in player_lookup:
                    match.player2 = player_lookup[pid2]

    def start_tournament(self):
        if not self.tournaments:
            self.view.display_message("Aucun tournoi disponible.")
            return

        self.show_all_tournaments()
        index = int(input("Sélectionnez un tournoi (index) : "))
        tournament = self.tournaments[index]
