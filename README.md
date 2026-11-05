# Student Manager

Application de bureau pour gérer les étudiants, les matières et les notes.
Elle repose sur une interface Tkinter et une base de données SQLite.

## Fonctionnalités

- **Étudiants** : consulter, ajouter, rechercher et supprimer des étudiants.
- **Notes** : enregistrer les notes par matière et consulter les résultats.
- **Statistiques** : nombre d'étudiants, moyenne générale, moyennes par étudiant et par classe.

## Prérequis

- Python 3.14 ou supérieur
- Tkinter (inclus avec Python sur Windows et macOS ; sous Linux : `sudo apt install python3-tk`)

## Installation

Depuis TestPyPI :

```bash
pip install --index-url https://test.pypi.org/simple/ <nom-du-package>
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

Danielle Maneche, Divine Omaty
