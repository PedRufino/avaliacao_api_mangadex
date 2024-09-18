from decorators.tratamento_erros import request_errors
import requests


class ApiModel:

    API_URL = "https://api.mangadex.org/manga"

    def __init__(self, params: dict = None):
        self.params = params or {"limit": 100, "offset": 0}

    @request_errors
    def _get(self, url: str, params: dict = None):
        """
        - Aplica o decorador para tratar erros e realizar tentativas em caso de falhas
        - Faz uma requisição GET para a URL fornecida com os parâmetros fornecidos
        """
        return requests.get(url, params=params)

    def get_all_manga(self):
        """Coleta todas as informações da API"""
        while True:
            yield self._get(self.API_URL, self.params)
            self.params["offset"] += 100

    def get_original_language(self, language: str):
        """Coleta dados filtrados por um idioma original"""
        self.params.update({"originalLanguage[]": language})

        while True:
            yield self._get(self.API_URL, self.params)
            self.params["offset"] += 100

    def get_available_languages(self, language: str):
        """Coleta dados filtrados por idiomas disponíveis"""
        self.params.update({"originalLanguage[]": language})

        while True:
            yield self._get(self.API_URL, self.params)
            self.params["offset"] += 100

    def get_name_manga(self, title: str):
        """Coleta dados com base no title informado"""
        self.params.update({"title": title})

        while True:
            yield self._get(self.API_URL, self.params)
            self.params["offset"] += 100
