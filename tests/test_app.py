import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_health_endpoint():
    with app.test_client() as c:
        r = c.get("/")
        assert r.status_code == 200
        assert r.get_json()["status"] == "ok"
