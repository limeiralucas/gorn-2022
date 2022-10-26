import json
import os

from sqlmodel import Session

from app.core.database import create_database_and_tables, engine
from app.core.models.database import Account, Offer, Purchase, State

session = Session(engine)
dir_path = os.path.dirname(os.path.realpath(__file__))
mock_path = os.path.join(dir_path, 'mocked_data')


def insert_mock_data(cls):
    with open(os.path.join(mock_path, f'{cls.__tablename__}.json')) as file:
        data = json.load(file)

    for row in data:
        session.add(cls(**row))

    session.commit()


def destroy_database():
    try:
        os.remove(os.path.join(dir_path, 'database.db'))
    except OSError:
        pass


if __name__ == '__main__':
    destroy_database()
    create_database_and_tables()
    for cls in (State, Account, Offer, Purchase):
        insert_mock_data(cls)
