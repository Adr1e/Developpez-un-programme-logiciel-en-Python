class Match:
    """
    Représente un match entre deux joueurs.
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None  # (score1, score2)

    def set_result(self, score1, score2):
        """
        Définit le résultat du match et met à jour les scores des joueurs.
        """
        self.result = (score1, score2)
        self.player1.score += score1
        self.player2.score += score2

    def to_dict(self):
        return {
            "player1": self.player1.national_id,
            "player2": self.player2.national_id,
            "result": self.result
        }

    def __repr__(self):
        if self.result:
            return f"{self.player1.first_name} vs {self.player2.first_name} : {self.result[0]} - {self.result[1]}"
        return f"{self.player1.first_name} vs {self.player2.first_name} : (en attente)"

    @classmethod
    def from_dict(cls, data):
        from models.player import Player  # Import local pour éviter les boucles

        # Créer des joueurs "vides" avec seulement l'identifiant
        player1 = Player("", "", "", data["player1"])
        player2 = Player("", "", "", data["player2"])

        match = cls(player1, player2)
        match.result = tuple(data["result"]) if data["result"] else None

        # Mettre à jour les scores si un résultat existe
        if match.result:
            player1.score += match.result[0]
            player2.score += match.result[1]

        return match
