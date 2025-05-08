from models import Student

def create_student(session, name: str, email: str) -> Student:
    student = Student(name=name, email=email)
    session.add(student)
    session.commit()
    return student

def update_student(session, email: str, new_name: str) -> Student:
    student = session.query(Student).filter_by(email=email).first()
    if student:
        student.name = new_name
        session.commit()
    return student

def delete_student(session, email: str) -> bool:
    student = session.query(Student).filter_by(email=email).first()
    if student:
        session.delete(student)
        session.commit()
        return True
    return False

def get_student_by_email(session, email: str) -> Student | None:
    return session.query(Student).filter_by(email=email).first()