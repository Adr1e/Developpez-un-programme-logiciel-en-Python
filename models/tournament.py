"""Modèle représentant un tournoi d'échecs."""


class Tournament:
    """
    Représente un tournoi avec plusieurs joueurs et tours.

    Attributes:
        name (str): Nom du tournoi.
        location (str): Lieu du tournoi.
        start_date (str): Date de début.
        end_date (str): Date de fin.
        time_control (str): Contrôle du temps (bullet, blitz, rapide).
        description (str): Remarques éventuelles.
        nb_rounds (int): Nombre de tours (défaut : 4).
        current_round (int): Numéro du tour en cours.
        players (list): Liste des joueurs inscrits.
        rounds (list): Liste des tours effectués.
    """

    def __init__(self, name, location, start_date, end_date, time_control, description="", nb_rounds=4):
        """Initialise un tournoi avec ses données de base."""
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.description = description
        self.nb_rounds = nb_rounds
        self.current_round = 0
        self.players = []
        self.rounds = []

    def add_player(self, player):
        """Ajoute un joueur à la liste des participants."""
        self.players.append(player)

    def add_round(self, round_obj):
        """Ajoute un tour et met à jour le compteur de tour."""
        self.rounds.append(round_obj)
        self.current_round += 1

    def has_more_rounds(self):
        """Vérifie s'il reste des rounds à jouer."""
        return self.current_round < self.nb_rounds

    def __str__(self):
        """Retourne une représentation lisible du tournoi."""
        return (
            f"Titre : {self.name} | Lieu : {self.location} | "
            f"Début : {self.start_date} | Fin : {self.end_date} | "
            f"Contrôle du temps : {self.time_control} | Rounds : {self.nb_rounds}"
        )

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour la sérialisation JSON."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "time_control": self.time_control,
            "description": self.description,
            "players": [player.to_dict() for player in self.players],
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "current_round": self.current_round,
            "nb_rounds": self.nb_rounds
        }

    @classmethod
    def from_dict(cls, data):
        tournament = cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            time_control=data["time_control"],
            description=data.get("description", ""),
            nb_rounds=data.get("nb_rounds", 4)
        )
        tournament.current_round = data.get("current_round", 0)

        from models.player import Player
        tournament.players = [Player.from_dict(
            p) for p in data.get("players", [])]

        from models.round import Round
        tournament.rounds = [Round.from_dict(r)
                             for r in data.get("rounds", [])]

        return tournament
