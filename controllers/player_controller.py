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
        new_player = Player(**player_data)
        self.players.append(new_player)
        self.save_players()

    def show_all_players(self):
        """Affiche tous les joueurs enregistrés."""
        self.view.display_players_list(self.players)

    def get_players_by_id(self):
        """Retourne un dictionnaire {national_id: player} pour tous les joueurs."""
        return {player.national_id: player for player in self.players}
