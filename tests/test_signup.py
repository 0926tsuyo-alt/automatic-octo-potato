def test_signup_valid_email_registers_student(client):
    # Arrange
    activity = "Swimming Club"
    email = "student@example.com"
    assert email not in client.get("/activities").json()[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]
    assert resp.json()["message"] == f"Signed up {email} for {activity}"


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "new@mergington.edu"

    # Act
    r1 = client.post(f"/activities/{activity}/signup", params={"email": email})
    r2 = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert r1.status_code == 200
    assert r2.status_code == 400


def test_unregister_removes_student(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"
    assert email in client.get("/activities").json()[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email not in client.get("/activities").json()[activity]["participants"]


def test_unregister_not_registered_returns_400(client):
    # Arrange
    activity = "Swimming Club"
    email = "nonexistent@example.com"

    # Act
    resp = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert resp.status_code == 400


def test_signup_nonexistent_activity_returns_404(client):
    # Act
    resp = client.post("/activities/NoSuchActivity/signup", params={"email":"a@b.c"})

    # Assert
    assert resp.status_code == 404
