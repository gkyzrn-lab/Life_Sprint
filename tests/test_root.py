from fastapi.testclient import TestClient

from main import app


def test_root_status_and_keys():
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.json()
    assert body.get("status") == "ok"
    assert "message" in body
    assert "routes" in body
