from models.player import Player
from views.player_view import PlayerView
from serializers.json_saver import save_data, load_data


class PlayerController:
    """Contrôleur pour gérer la logique autour des joueurs."""

    def __init__(self):
        self.view = PlayerView()
        self.filename = "data/players.json"
        self.players = self.load_players()

    def load_players(self):
        """Charge les joueurs existants depuis le fichier JSON."""
        try:
            return load_data(self.filename, Player)
        except FileNotFoundError:
            return []

    def save_players(self):
        """Sauvegarde la liste actuelle des joueurs dans le fichier JSON."""
        save_data(self.players, self.filename)

    def add_player(self):
        """Crée un nouveau joueur et l’enregistre."""
        player_data = self.view.get_player_info()

        # Vérification de doublon d'identifiant
        if any(p.national_id == player_data["national_id"] for p in self.players):
            self.view.display_message("Un joueur avec cet identifiant existe déjà.")
            return

        new_player = Player(
            first_name=player_data["first_name"],
            last_name=player_data["last_name"],
            birthdate=player_data["birthdate"],
            national_id=player_data["national_id"]
        )
        self.players.append(new_player)
        self.save_players()
        self.view.confirm_save(new_player)

    def show_all_players(self):
        """Affiche tous les joueurs enregistrés."""
        self.view.display_players_list(self.players)

    def get_players_by_id(self):
        """Retourne un dictionnaire {national_id: player} pour tous les joueurs."""
        return {player.national_id: player for player in self.players}
