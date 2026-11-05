from .database import get_connection


def add_grade(student_id, subject_id, grade):
    """
    Ajoute une note pour un étudiant et une matière.
    Retourne l'identifiant de la note créée.
    """

    with get_connection() as connection:
        cursor = connection.execute(
            (student_id, subject_id, grade)
        )

        return cursor.lastrowid


def get_grades_by_student(student_id):
    """
    Retourne les notes d'un étudiant avec le nom de la matière,
    """

    with get_connection() as connection:
        cursor = connection.execute(
            (student_id,)
        )

        return cursor.fetchall()


def get_student_average(student_id):
    """
    Retourne la moyenne d'un étudiant.
    """

    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT AVG(grade)
            FROM grades
            WHERE student_id = ?
            """,
            (student_id,)
        )

        result = cursor.fetchone()

        return result[0] if result[0] is not None else 0