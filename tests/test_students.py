import pytest

from student_manager_az.database import get_connection
from student_manager_az.students import (
    get_students,
    add_student,
    delete_student,
    search_students,
)


@pytest.fixture
def setup_database(tmp_path, monkeypatch):
    """Prépare une base SQLite temporaire pour les tests."""

    database_file = tmp_path / "test_students.db"

    def get_test_connection():
        import sqlite3
        return sqlite3.connect(database_file)

    monkeypatch.setattr(
        "student_manager_az.students.get_connection",
        get_test_connection,
    )

    with get_test_connection() as connection:
        connection.execute("""
            CREATE TABLE students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT,
                class_name TEXT
            )
        """)

    return database_file


def test_add_student(setup_database):
    """ vérifier l’ajout d’un étudiant """
    student_id = add_student(
        "Alice", "Martin", "alice@example.com", "BTS SIO"
    )

    assert student_id == 1


def test_get_students(setup_database):
    """Vérifie la récupération de la liste des étudiants."""

    add_student("Alice", "Martin", "alice@example.com", "BTS SIO")
    add_student("Bob", "Durand", "bob@example.com", "BTS SIO")

    students = get_students()

    assert students == [
        (2, "Bob", "Durand", "bob@example.com", "BTS SIO"),
        (1, "Alice", "Martin", "alice@example.com", "BTS SIO"),
    ]


def test_delete_student(setup_database):
    """Vérifie la suppression d'un étudiant."""
    alice_id = add_student("Alice", "Martin", "alice@example.com", "BTS SIO")
    add_student("Bob", "Durand", "bob@example.com", "BTS SIO")

    delete_student(alice_id)

    students = get_students()
    assert len(students) == 1
    assert students[0][2] == "Durand"


def test_search_students(setup_database):
    """Vérifie la recherche par nom et par prénom."""
    add_student("Alice", "Martin", "alice@example.com", "BTS SIO")
    add_student("Bob", "Durand", "bob@example.com", "BTS SIO")
    expected = [(1, "Alice", "Martin", "alice@example.com", "BTS SIO")]

    by_last_name = search_students("Martin")
    by_first_name = search_students("Alice")

    assert by_last_name == expected
    assert by_first_name == expected


def test_search_students_no_result(setup_database):
    """Vérifie qu'une recherche sans correspondance renvoie une liste vide."""
    add_student("Alice", "Martin", "alice@example.com", "BTS SIO")

    results = search_students("Inconnu")

    assert results == []