from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    """
    Page Object для страницы товара.
    """
    TITLE = (By.CLASS_NAME, 'product-detail-page__title')
    AUTHOR = (By.CLASS_NAME, 'product-authors')
    PRICE = (By.CLASS_NAME, 'product-offer-price__actual')
    DESCRIPTION = (By.CLASS_NAME, 'product-description-short__tex')
    ADD_TO_CART = (By.CLASS_NAME, 'chg-app-button chg-app-button--primary chg-app-button--l chg-app-button--breeze product-buttons__main-action product-buttons__main-action--stretch product-buttons__main-action product-buttons__main-action--stretch')

    def __init__(self, driver) -> None:
        """
        Инициализирует объект ProductPage.

        Args:
            driver: Объект WebDriver.

        Returns:
            None
        """
        self.driver = driver

    def is_displayed(self) -> bool:
        """
        Проверяет, отображаются ли ключевые элементы страницы.

        Returns:
            bool: True, если все элементы присутствуют.
        """
        elements = [self.TITLE, self.AUTHOR, self.PRICE, self.DESCRIPTION, self.ADD_TO_CART]
        for loc in elements:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))
        return True

    def add_to_cart(self) -> None:
        """
        Добавляет товар в корзину.

        Returns:
            None
        """
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        )
        add_button.click()
