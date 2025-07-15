import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import Base, Student
from db_utils import DATABASE_URL  # Убрали get_db

# Фикстура для создания сессии для каждого теста


@pytest.fixture(scope="function")
def db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)  # Создаем таблицы
    SessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(engine)  # Удаляем таблицы


def test_add_student(db):
    """Тест добавления студента."""
    new_student = Student(name="Alice", group="A1")
    db.add(new_student)
    db.commit()
    assert new_student.id is not None
    retrieved_student = db.query(Student).filter(
        Student.id == new_student.id).first()
    assert retrieved_student.name == "Alice"
    assert retrieved_student.group == "A1"


def test_update_student(db):
    """Тест изменения информации о студенте."""
    new_student = Student(name="Bob", group="B2")
    db.add(new_student)
    db.commit()
    student_id = new_student.id
    student_to_update = db.query(Student).filter(
        Student.id == student_id).first()
    student_to_update.name = "Charlie"
    student_to_update.group = "C3"
    db.commit()
    updated_student = db.query(Student).filter(
        Student.id == student_id).first()
    assert updated_student.name == "Charlie"
    assert updated_student.group == "C3"


def test_delete_student(db):
    """Тест удаления студента."""
    new_student = Student(name="David", group="D4")
    db.add(new_student)
    db.commit()
    student_id = new_student.id
    student_to_delete = db.query(Student).filter(
        Student.id == student_id).first()
    db.delete(student_to_delete)
    db.commit()
    deleted_student = db.query(Student).filter(
        Student.id == student_id).first()
    assert deleted_student is None
