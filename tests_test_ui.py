import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.ui
class TestUI:
    @pytest.fixture(autouse=True)
    def setup(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield driver
        driver.quit()

    @allure.title("Проверка работы строки поиска")
    @allure.description("Проверяет, что поиск возвращает результаты по запросу.")
    def test_search_function(self, setup):
        driver = setup
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step("Выполнить поиск по 'Бунин'"):
            main_page.search_for('Бунин')
        search_page = SearchResultsPage(driver)
        with allure.step("Проверить, что цены отображаются"):
            prices = search_page.get_prices()
            assert len(prices) > 0, "Нет результатов поиска"

    @allure.title("Проверка сортировки результатов")
    @allure.description("Проверяет сортировку по цене по возрастанию.")
    def test_sort_results(self, setup):
        driver = setup
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_for('Бунин')
        search_page = SearchResultsPage(driver)
        with allure.step("Выбрать сортировку по цене по возрастанию"):
            search_page.select_sort_by_price_asc()
        with allure.step("Проверить, что цены отсортированы"):
            prices = search_page.get_prices()
            assert search_page.is_sorted_asc(prices), "Цены не отсортированы по возрастанию"

    @allure.title("Проверка отображения страницы книги")
    @allure.description("Проверяет, что страница книги отображает ключевые элементы.")
    def test_product_page_display(self, setup):
        driver = setup
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_for('Бунин')
        search_page = SearchResultsPage(driver)
        with allure.step("Кликнуть на первый товар"):
            search_page.click_first_product()
        product_page = ProductPage(driver)
        with allure.step("Проверить отображение элементов"):
            assert product_page.is_displayed(), "Элементы страницы товара не отображаются"

    @allure.title("Проверка добавления книги в корзину")
    @allure.description("Проверяет добавление товара в корзину.")
    def test_add_to_cart(self, setup):
        driver = setup
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_for('Бунин')
        search_page = SearchResultsPage(driver)
        search_page.click_first_product()
        product_page = ProductPage(driver)
        with allure.step("Добавить в корзину"):
            product_page.add_to_cart()
        cart_page = CartPage(driver)
        cart_page.open()
        with allure.step("Проверить, что товар в корзине"):
            assert cart_page.has_item(), "Товар не добавлен в корзину"

    @allure.title("Проверка процесса оформления заказа")
    @allure.description("Проверяет полный процесс оформления заказа как гость.")
    def test_checkout_process(self, setup):
        driver = setup
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_for('Бунин')
        search_page = SearchResultsPage(driver)
        search_page.click_first_product()
        product_page = ProductPage(driver)
        product_page.add_to_cart()
        cart_page = CartPage(driver)
        cart_page.open()
        with allure.step("Перейти к оформлению"):
            cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(driver)
        with allure.step("Проверить видимость формы"):
            assert checkout_page.is_form_visible(), "Форма оформления не видна"
        with allure.step("Выбрать способ получения 'курьером'"):
            checkout_page.select_delivery_method_courier()
        with allure.step("Заполнить адрес: улица и номер дома, квартира"):
            checkout_page.fill_address('Улица Ленина, 10', '5')
        with allure.step("Выбрать службу доставки"):
            checkout_page.select_delivery_service('СДЭК')
        with allure.step("Выбрать способ оплаты 'при получении'"):
            checkout_page.select_payment_upon_receipt()
        with allure.step("Заполнить данные получателя: ФИО, email, телефон"):
            checkout_page.fill_recipient_details('Иванов Иван Иванович', 'email', '1234567890')
        with allure.step("Нажать 'Оформить заказ'"):
            checkout_page.submit_order()
