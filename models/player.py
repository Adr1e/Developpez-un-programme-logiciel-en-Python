"""Modèle représentant un joueur d'échecs."""


class Player:
    """
    Représente un joueur d'échecs.

    Attributs :
        first_name (str): Prénom du joueur.
        last_name (str): Nom de famille.
        birthdate (str): Date de naissance (JJ/MM/AAAA).
        national_id (str): Identifiant national d’échecs.
        score (float): Score du joueur pendant un tournoi.
    """

    def __init__(self, first_name, last_name, birthdate, national_id):
        """Initialise un joueur avec ses données personnelles."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.national_id = national_id
        self.score = 0.0

    def __repr__(self):
        """Retourne une représentation lisible du joueur."""
        return f"{self.first_name} {self.last_name} ({self.national_id})"

    def to_dict(self):
        """Sérialise le joueur en dictionnaire."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate,
            "national_id": self.national_id,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un joueur à partir d'un dictionnaire."""
        player = cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birthdate=data["birthdate"],
            national_id=data["national_id"]
        )
        player.score = data.get("score", 0.0)
        return player
