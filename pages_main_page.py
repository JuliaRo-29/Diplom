from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import config


class MainPage:
    """
    Page Object для главной страницы chitai-gorod.ru
    """
    SEARCH_FIELD = (By.CLASS_NAME, 'search-form__input search-form__input--search') 

    def __init__(self, driver) -> None:
        """
        Инициализирует объект MainPage.

        Args:
            driver: Объект WebDriver.

        Returns:
            None
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает главную страницу.

        Returns:
            None
        """
        self.driver.get(config.BASE_URL)

    def search_for(self, query: str) -> None:
        """
        Выполняет поиск по запросу.

        Args:
            query (str): Запрос для поиска.

        Returns:
            None
        """
        search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SEARCH_FIELD)
        )
        search_field.send_keys(query)
        search_field.send_keys(Keys.ENTER)
