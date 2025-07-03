import re
from datetime import datetime

class PlayerView:
    """Vue pour l'interaction avec les joueurs (console)."""

    def get_player_info(self):
        """Demande à l'utilisateur les informations d'un nouveau joueur avec validation."""

        print("\nCréation d'un nouveau joueur :")

        # Validation du prénom
        while True:
            first_name = input("Prénom : ").strip()
            if first_name.replace("-", "").isalpha():
                break
            print("Le prénom ne doit contenir que des lettres.")

        # Validation du nom
        while True:
            last_name = input("Nom : ").strip()
            if last_name.replace("-", "").isalpha():
                break
            print("Le nom ne doit contenir que des lettres.")

        # Validation de la date
        # Validation de la date
        while True:
            birthdate = input("Date de naissance (JJ/MM/AAAA) : ").strip()
            try:
                date_obj = datetime.strptime(birthdate, "%d/%m/%Y")
                if date_obj > datetime.today():
                    print(" La date de naissance ne peut pas être dans le futur.")
                    continue
                break
            except ValueError:
                print(" Format invalide. Utilise JJ/MM/AAAA.")


        # Validation de l'identifiant national
        while True:
            national_id = input("Identifiant national (ex: AB12345) : ").strip().upper()
            if re.match(r"^[A-Z]{2}\d{5}$", national_id):
                break
            print(" Format invalide. Il doit contenir 2 lettres suivies de 5 chiffres (ex: AB12345).")

        return {
            "first_name": first_name,
            "last_name": last_name,
            "birthdate": birthdate,
            "national_id": national_id
        }

    def display_players_list(self, players):
        print("\nListe des joueurs :")
        if not players:
            print("Aucun joueur enregistré.")
            return
        for player in players:
            print(f"- {player.first_name} {player.last_name} | ID : {player.national_id}")

    def confirm_save(self, player):
        print(f" Joueur {player.first_name} {player.last_name} enregistré avec succès.")

    def display_message(self, message):
        print(message)
