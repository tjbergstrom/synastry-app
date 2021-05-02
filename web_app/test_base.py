# test_base.py
#
# Run:
# $ py.test
# Or:
# $ python3 -m pytest


import flask
import os
import tempfile
import pytest
from webapp import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home(app, client):
    response = client.get("/")
    assert response.status_code == 200


def test_about(app, client):
    response = client.get("/about")
    assert response.status_code == 200


def test_match(app, client):
    response = client.get("/match")
    assert response.status_code == 200


def test_synastry(app, client):
    response = client.get("/synastry")
    assert response.status_code == 200


def test_none(app, client):
    response = client.get("/four-oh-four")
    assert response.status_code == 404


@pytest.mark.parametrize(('bday1', 'bday2', 'message'), (
    ('01/14/2000', '01/14/1999', b''),
    ('', '', b''),
))
def test_match(client, bday1, bday2, message):
    response = client.post(
        "/match",
        data={
            "" : bday1,
            "" : bday2
        }
    )
    assert message in response.data



##
