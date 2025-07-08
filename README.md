# Chess Tournament

Application de gestion de tournois d’échecs en local, développée en Python avec le modèle MVC.

## Fonctionnalités

- Ajouter des joueurs avec leur nom, prénom, date de naissance et identifiant national (format AB12345).
- Créer des tournois avec nom, lieu, dates, description et type de contrôle du temps (bullet, blitz, rapide).
- Lancer un tournoi avec appariement automatique sans doublon et saisie des scores.
- Sauvegarder les données localement en JSON (joueurs, tournois, rounds, matchs).
- Afficher les rounds, les matchs et le classement final du tournoi.
- Générer un rapport PEP8 avec flake8-html.

## Prérequis

- Python **3.9+**
- `pip` (inclus avec Python)

Vérifier votre version de Python :

```bash
python --version
```

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
├── flake-report/
│   └── index.html (rapport PEP8)
│
├── data/
│   ├── players.json
│   └── tournaments.json
│
├── main.py
├── requirements.txt
└── README.md
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
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Mettre à jour pip et installer les dépendances  
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Lancer le projet

```bash
python main.py
```

## Vérification PEP8 et rapport flake8

Pour vérifier que le code respecte les bonnes pratiques :

```bash
flake8 .
```

Pour générer un rapport HTML :

```bash
flake8 --format=html --htmldir=flake-report
```

Le rapport sera consultable dans `flake-report/index.html`.

(Optionnel) Pour reformater automatiquement le code :

```bash
autopep8 --in-place --recursive .
```

## Données

Les fichiers JSON sont générés automatiquement :

- `players.json` : contient tous les joueurs enregistrés.
- `tournaments.json` : contient tous les tournois créés.

Ces fichiers sont situés dans le dossier `data/`.

---

Projet réalisé en freelance pour un club d'échecs local.
