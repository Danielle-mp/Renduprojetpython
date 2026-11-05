from .database import get_connection


def get_students():
    """
    Retourne la liste de tous les étudiants.
    """

    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT id, first_name, last_name, email, class_name
            FROM students
            ORDER BY last_name, first_name
            """
        )

        return cursor.fetchall()


def add_student(first_name, last_name, email, class_name):
    """
    Ajoute un nouvel étudiant dans la base de données.
    Retourne l'identifiant du nouvel étudiant.
    """

    with get_connection() as connection:
        cursor = connection.execute(
            (first_name, last_name, email, class_name)
        )

        return cursor.lastrowid


def delete_student(student_id):
    """
    Supprime un étudiant.
    """

    with get_connection() as connection:
        connection.execute(
            (student_id,)
        )


def search_students(name):
    """
    Recherche un étudiant par son nom ou son prénom.
    """

    pattern = f"%{name}%"

    with get_connection() as connection:
        cursor = connection.execute(
            (pattern, pattern)
        )

        return cursor.fetchall()