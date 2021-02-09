import pytest
import requests


@pytest.mark.parametrize("user_name, job_type", [("Irina", "QA"), ("Mike D.", "programmer")])
def test_user_creation_valid(target_url, user_name, job_type):
    """Тест на метод POST /api/users"""
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = {'name': user_name, "job": job_type}
    r = requests.post(f'{target_url}/api/users', headers=headers, json=body, verify=False)
    assert r.status_code == 201
    response = r.json()
    assert response.get('name') == user_name
    assert response.get('job') == job_type


@pytest.mark.parametrize("user_id", [-1, True, 'Irina', "1234"])
def test_get_user_wrong_id(target_url, user_id):
    """Тест на метод GET /api/users/{id}"""
    r = requests.get(f'{target_url}/api/users/{user_id}')
    assert r.status_code == 404


@pytest.mark.parametrize("user_id, name, new_job_type", [(1, 'Irina', 'Lead'), (15, 'Mike', 'Master')])
def test_update_job_type(target_url, user_id, name, new_job_type):
    """Тест на метод PUT /api/users/{id}"""
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = {'name': name, "job": new_job_type}
    r = requests.put(f'{target_url}/api/users{user_id}', headers=headers, json=body, verify=False)
    assert r.status_code == 200
    response = r.json()
    assert response.get('job') == new_job_type


@pytest.mark.parametrize("user_id", [1, 15])
def test_delete_user_valid_id(target_url, user_id):
    """Тест на метод DELETE /api/users/{id}"""
    r = requests.delete(f'{target_url}/api/users/{user_id}')
    assert r.status_code == 204
