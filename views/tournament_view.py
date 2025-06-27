class TournamentView:
    """Vue pour l'interaction avec les tournois (console)."""

    def get_tournament_info(self):
        """Demande les informations pour créer un tournoi."""
        print("\n Création d'un nouveau tournoi :")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        start_date = input("Date de début (JJ/MM/AAAA) : ")
        end_date = input("Date de fin (JJ/MM/AAAA) : ")
        time_control = input("Contrôle du temps (blitz, bullet, rapide) : ")
        description = input("Description : ")
        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "time_control": time_control,
            "description": description
        }

    def confirm_save(self, tournament):
        """Message de confirmation de sauvegarde du tournoi."""
        print(f" Tournoi '{tournament.name}' sauvegardé avec succès.")

    def display_tournaments_list(self, tournaments):
        """Affiche la liste de tous les tournois."""
        print("\n Liste des tournois :")
        if not tournaments:
            print("Aucun tournoi trouvé.")
        for t in tournaments:
            print(f"- {t.name} à {t.location} du {t.start_date} au {t.end_date}")

    def display_message(self, message):
        print(f"\n {message}")
