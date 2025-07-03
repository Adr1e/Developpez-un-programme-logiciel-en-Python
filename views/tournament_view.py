from datetime import datetime

class TournamentView:
    """Vue pour l'interaction avec les tournois (console)."""

    def get_tournament_info(self):
        """Demande les informations pour créer un tournoi avec validation."""

        print("\nCréation d'un nouveau tournoi :")

        name = input("Nom du tournoi : ").strip()
        location = input("Lieu : ").strip()

        # Validation de la date de début
        while True:
            start_date_str = input("Date de début (JJ/MM/AAAA) : ").strip()
            try:
                start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
                break
            except ValueError:
                print("Format invalide. Utilise JJ/MM/AAAA.")

        # Validation de la date de fin
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

        # Contrôle du temps
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
        """Message de confirmation de sauvegarde du tournoi."""
        print(f"Tournoi '{tournament.name}' sauvegardé avec succès.")

    def display_tournaments_list(self, tournaments):
        """Affiche la liste de tous les tournois."""
        print("\nListe des tournois :")
        if not tournaments:
            print("Aucun tournoi trouvé.")
        for t in tournaments:
            print(f"- {t.name} à {t.location} du {t.start_date} au {t.end_date}")

    def display_message(self, message):
        print(f"\n{message}")
