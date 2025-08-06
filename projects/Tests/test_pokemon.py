import requests

BASE_URL = "https://api.pokemonbattle.ru/v2"
TRAINER_ID = "36313"
EXPECTED_NAME = "Tsukuyomi"

def test_get_trainers_status_code():
    response = requests.get(f"{BASE_URL}/trainers")
    assert response.status_code == 200

def test_trainer_name_in_response():
    response = requests.get(f"{BASE_URL}/trainers", params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200

    data = response.json()
    assert data["data"][0]["trainer_name"] == EXPECTED_NAME
