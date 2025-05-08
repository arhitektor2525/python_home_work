from student_crud import create_student, update_student, delete_student, get_student_by_email


def test_create_student(db_session):
    student = create_student(db_session, "Митрофан", "mitrofan@example.com")

    result = get_student_by_email(db_session, "mitrofan@example.com")
    assert result is not None
    assert result.name == "Митрофан"


def test_update_student(db_session):
    create_student(db_session, "Ефрасинья", "frosya@example.com")

    updated_student = update_student(db_session, "frosya@example.com", "Ефрасинья")
    assert updated_student.name == "Ефрасинья"

    result = get_student_by_email(db_session, "frosya@example.com")
    assert result.name == "Ефрасинья"


def test_delete_student(db_session):
    create_student(db_session, "Прохор", "prohor@example.com")

    delete_success = delete_student(db_session, "prohor@example.com")
    assert delete_success is True

    deleted_student = get_student_by_email(db_session, "prohor@example.com")
    assert deleted_student is None