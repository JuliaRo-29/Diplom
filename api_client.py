import requests
from typing import Dict, Optional
from config import API_BASE_URL


class ApiClient:
    """
    Клиент для работы с API chitai-gorod.ru.
    """
    def __init__(self, default_token: str) -> None:
        """
        Инициализирует API-клиент с базовым URL и токеном.

        Args:
            default_token (str): Токен авторизации по умолчанию.

        Returns:
            None
        """
        self.base_url = API_BASE_URL
        self.default_headers = {'Authorization': f'Bearer {default_token}'}

    def get(self, endpoint: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """
        Выполняет GET-запрос к указанному эндпоинту.

        Args:
            endpoint (str): Конечная точка API (например, '/search/facet-search').
            params (Optional[Dict]): Параметры запроса.
            headers (Optional[Dict]): Заголовки запроса (если None, используются default_headers).

        Returns:
            requests.Response: Ответ сервера.
        """
        url = f"{self.base_url}{endpoint}"
        headers = headers or self.default_headers
        return requests.get(url, headers=headers, params=params)

    def put(self, endpoint: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """
        Выполняет PUT-запрос к указанному эндпоинту.

        Args:
            endpoint (str): Конечная точка API (например, '/search/facet-search').
            params (Optional[Dict]): Параметры запроса.
            headers (Optional[Dict]): Заголовки запроса (если None, используются default_headers).

        Returns:
            requests.Response: Ответ сервера.
        """
        url = f"{self.base_url}{endpoint}"
        headers = headers or self.default_headers
        return requests.put(url, headers=headers, params=params)
