from datetime import datetime


class Round:
    """
    Représente un tour dans un tournoi.

    Attributes:
        name (str): Nom du tour.
        start_time (str): Date et heure de début.
        end_time (str): Date et heure de fin.
        matches (list): Liste de matchs.
    """

    def __init__(self, name):
        """Initialise un tour avec son nom et enregistre l'heure de début."""
        self.name = name
        self.start_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.end_time = None
        self.matches = []

    def end_round(self):
        """Enregistre l'heure de fin du tour."""
        self.end_time = datetime.now().strftime("%d/%m/%Y %H:%M")

    def add_match(self, match):
        """Ajoute un match à ce tour."""
        self.matches.append(match)

    def __repr__(self):
        """Affiche un résumé du round avec ses matchs."""
        match_list = "\n".join(str(match) for match in self.matches)
        return f"{self.name}:\n{match_list}"

    def to_dict(self):
        """Convertit le round en dictionnaire pour la sérialisation JSON."""
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [match.to_dict() for match in self.matches]
        }

    @classmethod
    def from_dict(cls, data):
        from models.match import Match  # Import ici pour éviter les import circulaires

        round_instance = cls(name=data["name"])
        round_instance.start_time = data.get("start_time")
        round_instance.end_time = data.get("end_time")
        round_instance.matches = [Match.from_dict(m) for m in data.get("matches", [])]

        return round_instance
