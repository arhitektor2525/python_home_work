from sqlalchemy import create_engine, text

class StudentTable:
    __scripts = {
        "insert": text("INSERT INTO students (name, email) VALUES (:name, :email)"),
        "select_by_email": text("SELECT * FROM students WHERE email = :email"),
        "update_name": text("UPDATE students SET name = :new_name WHERE email = :email"),
        "delete": text("DELETE FROM students WHERE email = :email")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_student(self, name: str, email: str):
        self.__db.execute(self.__scripts["insert"], {"name": name, "email": email})

    def get_student(self, email: str):
        return self.__db.execute(self.__scripts["select_by_email"], {"email": email}).fetchone()

    def update_student(self, email: str, new_name: str):
        self.__db.execute(self.__scripts["update_name"], {"new_name": new_name, "email": email})

    def delete_student(self, email: str):
        self.__db.execute(self.__scripts["delete"], {"email": email})