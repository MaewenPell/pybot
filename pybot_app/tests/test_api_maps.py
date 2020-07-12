import urllib.request
from io import BytesIO
import json

def test_http_run(monkeypatch):
    results = [
        {"place_id": "ChIJLU7jZClu5kcR4PcOOO6p3I0"}
    ]

    def monkeyreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', monkeyreturn)
    assert