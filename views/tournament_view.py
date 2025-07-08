from datetime import datetime
from prettytable import PrettyTable


class TournamentView:
    """Vue pour l'interaction avec les tournois (console)."""

    def get_tournament_info(self):
        """Demande les informations pour créer un tournoi avec validation."""
        print("\nCréation d'un nouveau tournoi :")

        name = input("Nom du tournoi : ").strip()
        location = input("Lieu : ").strip()

        while True:
            start_date_str = input("Date de début (JJ/MM/AAAA) : ").strip()
            try:
                start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
                break
            except ValueError:
                print("Format invalide. Utilise JJ/MM/AAAA.")

        while True:
            end_date_str = input("Date de fin (JJ/MM/AAAA) : ").strip()
            try:
                end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
                if end_date < start_date:
                    print("La date de fin ne peut pas être avant la date de début.")
                    continue
                break
            except ValueError:
                print("Format invalide. Utilise JJ/MM/AAAA.")

        valid_controls = ["bullet", "blitz", "rapide"]
        while True:
            time_control = input("Contrôle du temps (bullet, blitz, rapide) : ").strip().lower()
            if time_control in valid_controls:
                break
            print("Choix invalide. Options valides : bullet, blitz, rapide.")

        description = input("Description : ").strip()

        return {
            "name": name,
            "location": location,
            "start_date": start_date_str,
            "end_date": end_date_str,
            "time_control": time_control,
            "description": description
        }

    def confirm_save(self, tournament):
        print(f"Tournoi '{tournament.name}' sauvegardé avec succès.")

    def display_tournaments_list(self, tournaments):
        """Affiche la liste de tous les tournois."""
        print("\nListe des tournois :")
        if not tournaments:
            print("Aucun tournoi trouvé.")
        for i, t in enumerate(tournaments):
            print(f"{i} - {t.name} à {t.location} du {t.start_date} au {t.end_date}")

    def display_message(self, message):
        print(f"\n{message}")

    def display_tournament_report(self, tournament):
        """Affiche uniquement le classement final du tournoi sélectionné."""
        print("\n=== Tournament Report ===")
        print(f"Name: {tournament.name}")
        print(f"Location: {tournament.location}")
        print(f"Dates: {tournament.start_date} to {tournament.end_date}")
        print(f"Time control: {tournament.time_control}")
        print(f"Description: {tournament.description}")

        if not tournament.rounds:
            print("Ce tournoi n’a pas encore de rounds.")
            return

        print("\nClassement final :")
        sorted_players = sorted(tournament.players, key=lambda p: p.score, reverse=True)
        table = PrettyTable()
        table.field_names = ["Rang", "Joueur", "Score"]
        for i, player in enumerate(sorted_players, 1):
            table.add_row([i, f"{player.first_name} {player.last_name}", player.score])
        print(table)
