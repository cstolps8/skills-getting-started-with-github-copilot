import copy
import pytest
from fastapi.testclient import TestClient

import src.app as app_module


# Keep an immutable snapshot of the initial activities so tests can reset state
INITIAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Arrange: restore in-memory activities before each test to ensure isolation."""
    app_module.activities = copy.deepcopy(INITIAL_ACTIVITIES)
    yield
    app_module.activities = copy.deepcopy(INITIAL_ACTIVITIES)


@pytest.fixture
def client():
    return TestClient(app_module.app)


def test_get_activities_returns_all(client):
    # Arrange
    expected = copy.deepcopy(INITIAL_ACTIVITIES)

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    assert resp.json() == expected


def test_signup_success(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    assert email not in app_module.activities[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert resp.json().get("message") == f"Signed up {email} for {activity}"
    assert email in app_module.activities[activity]["participants"]


def test_signup_duplicate_fails(client):
    # Arrange
    activity = "Chess Club"
    email = app_module.activities[activity]["participants"][0]

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 400
    assert "already" in resp.json().get("detail", "").lower()


def test_signup_nonexistent_activity(client):
    # Arrange
    activity = "No Such Activity"
    email = "someone@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 404


def test_unregister_success(client):
    # Arrange
    activity = "Chess Club"
    email = app_module.activities[activity]["participants"][0]
    assert email in app_module.activities[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert resp.json().get("message") == f"Unregistered {email} from {activity}"
    assert email not in app_module.activities[activity]["participants"]


def test_unregister_not_registered(client):
    # Arrange
    activity = "Chess Club"
    email = "notregistered@mergington.edu"
    assert email not in app_module.activities[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert resp.status_code == 400


def test_unregister_nonexistent_activity(client):
    # Arrange
    activity = "No Such Activity"
    email = "someone@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert resp.status_code == 404
