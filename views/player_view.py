class PlayerView:
    """Vue pour l'interaction avec les joueurs (console)."""

    def get_player_info(self):
        """Demande à l'utilisateur les informations d'un nouveau joueur."""
        print("\n Création d'un nouveau joueur :")
        first_name = input("Prénom : ")
        last_name = input("Nom : ")
        birthdate = input("Date de naissance (JJ/MM/AAAA) : ")
        gender = input("Genre (H/F) : ")
        national_id = input("Identifiant national (ex: ABC123) : ")
        ranking = int(input("Classement (Elo) : "))
        return {
            "first_name": first_name,
            "last_name": last_name,
            "birthdate": birthdate,
            "gender": gender,
            "national_id": national_id,
            "ranking": ranking
        }

    def display_players_list(self, players):
        """Affiche la liste des joueurs enregistrés."""
        print("\n Liste des joueurs :")
        if not players:
            print("Aucun joueur enregistré.")
            return
        for player in players:
            print(f"- {player.first_name} {player.last_name} (Elo : {player.ranking})")

    def confirm_save(self, player):
        """Affiche un message confirmant l’enregistrement d’un joueur."""
        print(f" Joueur {player.first_name} {player.last_name} enregistré avec succès.")

    def display_message(self, message):
        """Affiche un message générique."""
        print(message)
