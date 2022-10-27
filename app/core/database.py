from sqlmodel import SQLModel, create_engine

from app.core.config import settings

engine = create_engine(
    f'sqlite:///{settings.SQLITE_FILE_NAME}',
    echo=False,
    connect_args={
        'check_same_thread': False
    }
)


def create_database_and_tables():
    SQLModel.metadata.create_all(engine)
