import pytest

from student_manager_az import database
from student_manager_az.subjects import get_subjects


@pytest.fixture
def setup_database(tmp_path, monkeypatch):
    """Prépare une base temporaire contenant la table subjects."""
    monkeypatch.setattr(
        database,
        "DATABASE_NAME",
        str(tmp_path / "test_subjects.db"),
    )
    database.init_database()


def test_get_subjects(setup_database):
    """Vérifie la récupération des matières enregistrées."""
    subjects = get_subjects()

    assert [name for _, name in subjects] == [
        "Python",
        "Réseaux",
        "SQL",
        "Systèmes",
        "Web",
    ]


def test_get_subjects_empty(setup_database):
    """Vérifie le comportement quand la table ne contient aucune matière."""

    with database.get_connection() as connection:
        connection.execute("DELETE FROM subjects")

    subjects = get_subjects()

    assert subjects == []