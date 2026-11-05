import pytest

from student_manager_az import database
from student_manager_az.grades import (
    add_grade,
    get_grades_by_student,
    get_student_average,
)
from student_manager_az.students import add_student

PYTHON_ID = 1
SQL_ID = 2


@pytest.fixture
def setup_database(tmp_path, monkeypatch):
    """
    Retourne l'identifiant de l'étudiant créé.
    """
    monkeypatch.setattr(
        database,
        "DATABASE_NAME",
        str(tmp_path / "test_grades.db"),
    )
    database.init_database()

    return add_student("Alice", "Martin", "alice@example.com", "BTS SIO")


def test_add_grade(setup_database):
    """Vérifie l'ajout d'une note."""
    student_id = setup_database
    add_grade(student_id, PYTHON_ID, 15)
    assert get_grades_by_student(student_id) == [(1, "Python", 15.0)]


def test_get_grades_by_student(setup_database):
    """Vérifie la récupération des notes d'un étudiant donné."""
    student_id = setup_database
    other_id = add_student("Bob", "Durand", "bob@example.com", "BTS SIO")
    add_grade(student_id, PYTHON_ID, 12)
    add_grade(student_id, SQL_ID, 15)
    add_grade(other_id, PYTHON_ID, 8)

    grades = get_grades_by_student(student_id)

    assert grades == [(1, "Python", 12.0), (2, "SQL", 15.0)]


def test_get_student_average(setup_database):
    """Vérifie le calcul de la moyenne d'un étudiant ayant des notes."""
    student_id = setup_database
    add_grade(student_id, PYTHON_ID, 10)
    add_grade(student_id, SQL_ID, 15)

    average = get_student_average(student_id)

    assert average == pytest.approx(12.5)


def test_get_student_average_without_grades(setup_database):
    """Vérifie que la moyenne d'un étudiant sans note vaut 0."""
    average = get_student_average(setup_database)

    assert average == 0