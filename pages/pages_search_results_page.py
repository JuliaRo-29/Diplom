from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage:
    """
    Page Object для страницы результатов поиска.
    """
    SORT_DROPDOWN = (By.CLASS_NAME, 'chg-app-select chg-app-custom-dropdown-wrapper app-catalog__sorting')  # Локатор для дропдауна сортировки
    PRICE_ITEMS = (By.XPATH, "//div[@class='chg-app-dropdown-custom-item' and text()='Сначала дешевые']")  # Локатор цен товаров

    def __init__(self, driver) -> None:
        """
        Инициализирует объект SearchResultsPage.

        Args:
            driver: Объект WebDriver.

        Returns:
            None
        """
        self.driver = driver

    def select_sort_by_price_asc(self) -> None:
        """
        Выбирает сортировку по цене по возрастанию.

        Returns:
            None
        """
        sort_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        )
        sort_dropdown.click()
        asc_option = self.driver.find_element(By.XPATH, "//div[@class='chg-app-dropdown-custom-item' and text()='Сначала дешевые']")
        asc_option.click()

    def get_prices(self) -> list[float]:
        """
        Получает список цен на странице.

        Returns:
            list[float]: Список цен.
        """
        price_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.PRICE_ITEMS)
        )
        prices = [float(p.text.replace(' ₽', '').replace(' ', '')) for p in price_elements]
        return prices

    def is_sorted_asc(self, prices: list[float]) -> bool:
        """
        Проверяет, отсортированы ли цены по возрастанию.

        Args:
            prices (list[float]): Список цен.

        Returns:
            bool: True, если отсортировано.
        """
        return all(prices[i] <= prices[i+1] for i in range(len(prices)-1))

    def click_first_product(self) -> None:
        """
        Кликает на первый товар в результатах.

        Returns:
            None
        """
        first_product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='app-products-list app-catalog__list'][0]"))
        )
        first_product.click()
