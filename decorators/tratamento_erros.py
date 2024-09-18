from functools import wraps
import requests
import time


def request_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        max_retries = 3  # Número máximo de tentativas
        attempt = 0

        while attempt < max_retries:
            try:
                response = func(*args, **kwargs)
                if response.status_code == 400:
                    attempt += 1
                    time.sleep(1)
                    continue
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as http_err:
                print(f"Ocorreu um erro HTTP: {http_err}")
                return None
            except requests.exceptions.RequestException as req_err:
                print(f"Ocorreu um erro: {req_err}")
                return None

        # Se o máximo de tentativas for atingido, retorna None
        return None

    return wrapper
