import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student

@pytest.fixture(scope="function")
def db_session():

    engine = create_engine("postgresql+psycopg2://postgres:Mu7.rm23.m32@localhost:5432/postgres")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session

    session.query(Student).delete()
    session.commit()
    session.close()