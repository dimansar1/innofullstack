import requests as rq
from streamlit import session_state
from typing import Optional

from patterns.cookie import controller

BACKEND_URL = "http://127.0.0.1:8000"

FAVOURITES_ENDPOINT = f'{BACKEND_URL}/favourites'
TANKS_ENDPOINT = f'{BACKEND_URL}/tanks'
AUTH_ENDPOINT = f'{BACKEND_URL}/auth'
USER_ENDPOINT = f'{BACKEND_URL}/users'

def request_with_authorization_header(
    request_type: str,
    endpoint: str,
    params: Optional[dict] = None,
    payload: Optional[dict] = None,
) -> rq.Response:
    headers = {
        "Authorization": f"Bearer {controller.get('access_token')}"
    }

    if request_type == "GET":
        response = rq.get(endpoint, headers=headers, params=params)
    elif request_type == "POST":
        response = rq.post(endpoint, headers=headers, params=params, json=payload)
    elif request_type == "PATCH":
        response = rq.patch(endpoint, headers=headers, params=params, json=payload)
    elif request_type == "DELETE":
        response = rq.delete(endpoint, headers=headers, params=params)
    else:
        raise ValueError("Неизвестный тип запроса")

    if response.status_code == 401:
        controller.remove("access_token")
        session_state.pop("profile", None)

    return response

def request(
    request_type: str,
    endpoint: str,
    params: Optional[dict] = None,
    payload: Optional[dict] = None,
) -> rq.Response:
    if request_type == "GET":
        response = rq.get(endpoint, params=params)
    elif request_type == "POST":
        response = rq.post(endpoint, params=params, json=payload)
    elif request_type == "PATCH":
        response = rq.patch(endpoint, params=params, json=payload)
    elif request_type == "DELETE":
        response = rq.delete(endpoint, params=params)
    else:
        raise ValueError("Неизвестный тип запроса")

    if response.status_code == 401:
        controller.remove("access_token")
        session_state.pop("profile", None)

    return response

def register(email: str, password: str, nickname: str) -> rq.Response:
    data = {
        "nickname": nickname,
        "email": email,
        "password": password,
    }
    return rq.post(f'{AUTH_ENDPOINT}/register', json=data)


def login(email: str, password: str) -> rq.Response:
    data = {
        "email": email,
        "password": password,
    }
    return rq.post(f'{AUTH_ENDPOINT}/login', json=data)

def get_error_message(response: rq.Response) -> str:
    try:
        detail = response.json().get("detail")
        return str(detail or f"Ошибка backend: HTTP {response.status_code}")
    except ValueError:
        return f"Ошибка backend: HTTP {response.status_code}"


def get_my_user():
    return request_with_authorization_header('GET', f'{USER_ENDPOINT}/users/me')


def get_tanks():
    return request('GET', TANKS_ENDPOINT)

def get_tank(tank_id: int):
    return request('GET', f'{TANKS_ENDPOINT}/{tank_id}')



def get_favourites():
    return request_with_authorization_header('GET', FAVOURITES_ENDPOINT)

def get_favourite_by_tank_id(tank_id: int):
    return request_with_authorization_header('GET', f'{FAVOURITES_ENDPOINT}/{tank_id}')

def add_favourite(tank_id: int):
    return request_with_authorization_header('POST', f'{FAVOURITES_ENDPOINT}/{tank_id}')

def remove_favourite(tank_id: int):
    return request_with_authorization_header('DELETE', f'{FAVOURITES_ENDPOINT}/{tank_id}')


if __name__ == '__main__':
    pass
