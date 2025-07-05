from models.tournament import Tournament
from models.round import Round
from models.match import Match
from serializers.json_saver import save_data, load_data
from views.tournament_view import TournamentView
from itertools import combinations
from prettytable import PrettyTable


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

        self.resolve_players(tournament)

        if not tournament.players:
            from controllers.player_controller import PlayerController
            pc = PlayerController()

            if len(pc.players) < 2:
                self.view.display_message("Pas assez de joueurs enregistrés pour commencer un tournoi.")
                return

            tournament.players.extend(pc.players[:])
            print(f"{len(pc.players)} joueurs ont été ajoutés automatiquement au tournoi.")

        def get_played_pairs(tournament):
            played = set()
            for round_ in tournament.rounds:
                for match in round_.matches:
                    pair = tuple(sorted((match.player1.national_id, match.player2.national_id)))
                    played.add(pair)
            return played

        all_possible_pairs = list(combinations(tournament.players, 2))
        total_pairs = len(all_possible_pairs)
        played_pairs = get_played_pairs(tournament)

        while len(played_pairs) < total_pairs and tournament.current_round < 4:
            round_name = f"Round {tournament.current_round + 1}"
            new_round = Round(round_name)
            used_players = set()
            round_matches = []

            for p1, p2 in all_possible_pairs:
                pair = tuple(sorted((p1.national_id, p2.national_id)))
                if pair in played_pairs:
                    continue
                if p1.national_id in used_players or p2.national_id in used_players:
                    continue

                round_matches.append((p1, p2))
                used_players.update([p1.national_id, p2.national_id])
                played_pairs.add(pair)

            if not round_matches:
                print("Plus de matchs possibles sans doublon — fin du tournoi.")
                break

            print(f"\n=== Début du {round_name} ===")
            for match_index, (p1, p2) in enumerate(round_matches, start=1):
                print(f"\nMatch {match_index} du {round_name} : {p1.first_name} vs {p2.first_name}")
                print("(Enter score: 1 = win, 0.5 = draw, 0 = loss or type 'pause' to stop)")

                while True:
                    score1_input = input(f"Score for {p1.first_name} : ").strip()
                    if score1_input.lower() == "pause":
                        print("Tournoi mis en pause. Vous pouvez le reprendre plus tard.")
                        self.save_tournaments()
                        return
                    try:
                        score1 = float(score1_input)
                        if score1 in [0, 0.5, 1]:
                            break
                    except ValueError:
                        pass
                    print("Entrée invalide. Utilisez uniquement 1, 0.5 ou 0.")

                while True:
                    score2_input = input(f"Score for {p2.first_name} : ").strip()
                    if score2_input.lower() == "pause":
                        print("Tournoi mis en pause. Vous pouvez le reprendre plus tard.")
                        self.save_tournaments()
                        return
                    try:
                        score2 = float(score2_input)
                        if score2 in [0, 0.5, 1]:
                            break
                    except ValueError:
                        pass
                    print("Entrée invalide. Utilisez uniquement 1, 0.5 ou 0.")

                match = Match(p1, p2)
                match.set_result(score1, score2)
                new_round.add_match(match)

            new_round.end_round()
            tournament.add_round(new_round)
            self.save_tournaments()
            print(f"\n{round_name} terminé et sauvegardé.")
            self.show_tournament_rounds(tournament)

        print("\nLe tournoi est terminé ! Classement final :")
        self.show_final_ranking(tournament)

    def show_final_ranking(self, tournament):
        sorted_players = sorted(tournament.players, key=lambda p: p.score, reverse=True)
        table = PrettyTable()
        table.field_names = ["Rank", "Player", "Score"]
        for i, player in enumerate(sorted_players, 1):
            table.add_row([i, f"{player.first_name} {player.last_name}", player.score])
        print(table)

    def show_tournament_rounds(self, tournament):
        if not tournament.rounds:
            print("Aucun round n’a encore été joué.")
            return

        print("\nRécapitulatif des rounds :")
        for round_ in tournament.rounds:
            print(f"\n{round_.name} | Début : {round_.start_time} | Fin : {round_.end_time}")
            for match in round_.matches:
                print(f" → {match}")

    def show_tournament_report(self):
        if not self.tournaments:
            self.view.display_message("Aucun tournoi enregistré.")
            return

        self.show_all_tournaments()
        index = int(input("Sélectionnez un tournoi (index) : "))
        tournament = self.tournaments[index]
        self.resolve_players(tournament)
        self.view.display_tournament_report(tournament)

    def show_tournament_reports(self):
        if not self.tournaments:
            self.view.display_message("Aucun tournoi disponible.")
            return

        self.view.display_tournaments_list(self.tournaments)
        try:
            index = int(input("Sélectionnez un tournoi (index) : "))
            tournament = self.tournaments[index]
        except (ValueError, IndexError):
            self.view.display_message("Index invalide.")
            return

        self.resolve_players(tournament)
        sorted_players = sorted(tournament.players, key=lambda p: p.score, reverse=True)

        print("\n=== Tournament Report ===")
        print(f"Name: {tournament.name}")
        print(f"Location: {tournament.location}")
        print(f"Dates: {tournament.start_date} to {tournament.end_date}")
        print(f"Time control: {tournament.time_control}")
        print(f"Description: {tournament.description}")
        print()

        table = PrettyTable()
        table.field_names = ["Rank", "Player", "Score"]

        for i, player in enumerate(sorted_players, 1):
            table.add_row([i, f"{player.first_name} {player.last_name}", player.score])

        print(table)
