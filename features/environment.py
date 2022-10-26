from behave.runner import Context
from fastapi.testclient import TestClient

from app.main import app


def before_all(context: Context):
    context.client = TestClient(app)
