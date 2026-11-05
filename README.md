# Student Manager

Application de bureau pour gérer les étudiants, les matières et les notes.
Elle repose sur une interface graphique Tkinter et une base de données SQLite.

## Fonctionnalités

- **Étudiants** : consulter, ajouter, rechercher (par nom ou prénom) et supprimer des étudiants.
- **Notes** : enregistrer la note d'un étudiant dans une matière et consulter ses résultats.
- **Statistiques** : nombre d'étudiants, moyenne générale, moyenne d'un étudiant et moyennes par classe.

## Prérequis

- Python 3.14 ou supérieur
- Tkinter (inclus avec Python sur Windows et macOS ; sous Linux : `sudo apt install python3-tk`)

Aucune autre dépendance n'est nécessaire : l'application utilise uniquement la
bibliothèque standard (`tkinter` et `sqlite3`).

## Installation

Depuis TestPyPI :

```bash
pip install --index-url https://test.pypi.org/simple/ student-manager
```

## Lancement

```bash
python -m student_manager_az.main
```

La base de données `student_manager.db` est créée dans le dossier depuis lequel
l'application est lancée.

## Développement

```bash
poetry install
poetry run pytest
```

## Auteurs

Danielle Maneche et Divine Omaty
