def test_get_activities_returns_dict(client):
    # Arrange: fixtures set up a known state
    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
