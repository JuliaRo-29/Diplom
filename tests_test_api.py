import pytest
import requests
import allure
from config import API_BASE_URL, API_TOKEN, CITY_ID


@pytest.mark.api
class TestAPI:
    headers = {'Authorization': f'Bearer {API_TOKEN}'}

    @allure.title("Поиск по названию на кириллице")
    @allure.description("Проверяет поиск по кириллическому запросу.")
    def test_search_kirillica(self):
        params = {'customerCityId': CITY_ID, 'phrase': 'Бунин'}
        response = requests.get(f'{API_BASE_URL}/search/facet-search', headers=self.headers, params=params)
        with allure.step("Проверить статус 200"):
            assert response.status_code == 200
        data = response.json()
        with allure.step("Проверить наличие результатов"):
            assert len(data.get('data', {}).get('products', {}).get('items', [])) > 0

    @allure.title("Поиск по названию на латинице")
    @allure.description("Проверяет поиск по запросу на латинице.")
    def test_search_latin(self):
        params = {'customerCityId': CITY_ID, 'phrase': 'the choice'}
        response = requests.get(f'{API_BASE_URL}/search/facet-search', headers=self.headers, params=params)
        with allure.step("Проверить статус 200"):
            assert response.status_code == 200
        data = response.json()
        with allure.step("Проверить наличие результатов"):
            assert len(data.get('data', {}).get('products', {}).get('items', [])) > 0

    @allure.title("Поиск с пустым запросом")
    @allure.description("Проверяет обработку пустого запроса.")
    def test_search_empty(self):
        params = {'customerCityId': CITY_ID, 'phrase': ''}
        response = requests.get(f'{API_BASE_URL}/search/facet-search', headers=self.headers, params=params)
        with allure.step("Проверить статус 400 или сообщение об ошибке"):
            assert response.status_code in [400, 200]

    @allure.title("Поиск с неактуальным токеном")
    @allure.description("Проверяет поиск с использованием невалидного токена авторизации.")
    def test_search_invalid_token(self):
        invalid_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyNDYzODA4LCJpYXQiOjE3NDc2ODUxMTMsImV4cCI6MTc0NzY4ODcxMywidHlwZSI6MjB9.e6MeKG__DTT6CrQJIHbqtaCnTkFFPlcg4BaLtlcDXC'
        headers = {'Authorization': f'Bearer {invalid_token}'}
        params = {'customerCityId': CITY_ID, 'phrase': 'Бунин'}
        response = requests.get(f'{API_BASE_URL}/search/facet-search', headers=headers, params=params)
        with allure.step("Проверить статус 401 Unauthorized"):
            assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"

    @allure.title("Поиск с другим методом (PUT)")
    @allure.description("Проверяет использование неверного метода.")
    def test_search_wrong_method(self):
        params = {'customerCityId': CITY_ID, 'phrase': 'Бунин'}
        response = requests.put(f'{API_BASE_URL}/search/facet-search', headers=self.headers, params=params)
        with allure.step("Проверить статус 405 Method Not Allowed"):
            assert response.status_code == 405
