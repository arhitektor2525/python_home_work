from Student_table import StudentTable

DB_CONNECTION = "postgresql+psycopg2://postgres:Mu7.rm23.m32@localhost:5432/postgres"
student_db = StudentTable(DB_CONNECTION)

def test_create_student():
    # Создание и проверка
    student_db.create_student("Митрофан", "mitrofan@example.com")
    result = student_db.get_student("mitrofan@example.com")
    assert result is not None
    assert result["name"] == "Митрофан"
    # Очистка
    student_db.delete_student("mitrofan@example.com")

def test_update_student():
    # Подготовка данных
    student_db.create_student("Ефрасинья", "frosya@example.com")
    # Обновление и проверка
    student_db.update_student("frosya@example.com", "Новая Ефрасинья")
    updated = student_db.get_student("frosya@example.com")
    assert updated["name"] == "Новая Ефрасинья"
    # Очистка
    student_db.delete_student("frosya@example.com")

def test_delete_student():
    # Подготовка данных
    student_db.create_student("Прохор", "prohor@example.com")
    # Удаление и проверка
    student_db.delete_student("prohor@example.com")
    deleted = student_db.get_student("prohor@example.com")
    assert deleted is None
