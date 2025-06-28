from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_breadcrumbs():
    data = {"conversation_id": "conv1", "step": 1, "content": "hello"}
    resp = client.post("/breadcrumbs/", json=data)
    assert resp.status_code == 200
    created = resp.json()
    assert created["step"] == 1
    resp = client.get("/breadcrumbs/conv1")
    assert resp.status_code == 200
    items = resp.json()
    assert len(items) == 1
    assert items[0]["content"] == "hello"
