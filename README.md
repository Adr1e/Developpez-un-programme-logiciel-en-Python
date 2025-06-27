# Chess Tournament

Application de gestion de tournois d’échecs en local, développée en Python avec le modèle MVC.

## Fonctionnalités

- Ajouter des joueurs avec leur nom, prénom, date de naissance, identifiant national, et classement Elo.
- Créer des tournois avec nom, lieu, date, description et type de contrôle du temps.
- Lancer un tournoi avec appairage automatique et saisie des scores.
- Sauvegarder les données en JSON (joueurs, tournois, rounds, matchs).
- Afficher les rounds et le classement final du tournoi.

## Structure du projet

```
chess_tournament/
│
├── controllers/
│   ├── player_controller.py
│   └── tournament_controller.py
│
├── models/
│   ├── player.py
│   ├── round.py
│   ├── tournament.py
│   └── match.py
│
├── serializers/
│   └── json_saver.py
│
├── views/
│   ├── player_view.py
│   └── tournament_view.py
│
├── main.py
└── requirements.txt
```

## Installation

1. Cloner le projet  
```bash
git clone <url_du_repo>
cd chess_tournament
```

2. Créer un environnement virtuel  
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Installer les dépendances  
```bash
pip install -r requirements.txt
```

## Lancer le projet

```bash
python main.py
```

## Nettoyage du code

Pour vérifier la conformité PEP8 avec flake8 :

```bash
flake8 .
```

Pour appliquer automatiquement certaines corrections :

```bash
autopep8 --in-place --recursive .
```

## Données

Les fichiers JSON générés automatiquement sont :

- players.json : tous les joueurs enregistrés
- tournaments.json : tous les tournois créés
