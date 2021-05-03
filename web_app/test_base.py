# test_base.py
#
# $ python3 -m pytest


import flask
import pytest
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home(app, client):
    response = client.get("/")
    assert response.status_code == 200


def test_match(app, client):
    response = client.get("/match")
    assert response.status_code == 200


def test_synastry(app, client):
    response = client.get("/synastry")
    assert response.status_code == 200


@pytest.mark.parametrize(('bday1', 'bday2', 'message'), (
    ('01/14/2000', '01/14/1999', b''),
))
def test_calc(client, bday1, bday2, message):
    response = client.post(
        "/match",
        data={
            "" : bday1,
            "" : bday2
        }
    )
    assert message in response.data



##
