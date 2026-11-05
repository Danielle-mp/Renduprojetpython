import pytest

from student_manager_az import database
from student_manager_az.grades import add_grade
from student_manager_az.statistics import (
    get_class_average,
    get_general_average,
    get_student_count,
)
from student_manager_az.students import add_student

PYTHON_ID = 1
SQL_ID = 2


@pytest.fixture
def setup_database(tmp_path, monkeypatch):
    """Prépare une base temporaire avec des étudiants, des classes et des notes."""
    monkeypatch.setattr(
        database,
        "DATABASE_NAME",
        str(tmp_path / "test_statistics.db"),
    )
    database.init_database()

    alice = add_student("Alice", "Martin", "alice@example.com", "B2_DEV1")
    bob = add_student("Bob", "Durand", "bob@example.com", "B2_DEV1")
    chloe = add_student("Chloé", "Petit", "chloe@example.com", "B2_DEV2")
    add_student("Dan", "Leroy", "dan@example.com", "B2_DEV3")  # sans note

    add_grade(alice, PYTHON_ID, 10)
    add_grade(alice, SQL_ID, 14)
    add_grade(bob, PYTHON_ID, 12)
    add_grade(chloe, PYTHON_ID, 20)


def test_get_student_count(setup_database):
    """Vérifie le nombre total d'étudiants enregistrés."""
    assert get_student_count() == 4


def test_get_general_average(setup_database):
    """Vérifie le calcul de la moyenne générale."""
    # (10 + 14 + 12 + 20) / 4
    assert get_general_average() == pytest.approx(14.0)


def test_get_class_average(setup_database):
    """Vérifie le calcul de la moyenne d'une classe donnée."""
    # B2_DEV1 : (10 + 14 + 12) / 3
    assert get_class_average("B2_DEV1") == pytest.approx(12.0)


def test_get_class_average_without_grades(setup_database):
    """Vérifie que la moyenne d'une classe sans note vaut 0."""
    assert get_class_average("B2_DEV3") == 0