from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config


class CartPage:
    """
    Page Object для страницы корзины.
    """
    CART_ITEM = (By.CLASS_NAME, 'chg-app-button chg-app-button--primary chg-app-button--l chg-app-button--light-green product-buttons__main-action product-buttons__main-action--stretch product-buttons__main-action product-buttons__main-action--stretch')
    CHECKOUT_BUTTON = (By.CLASS_NAME, 'chg-app-button chg-app-button--primary chg-app-button--l chg-app-button--breeze chg-app-button--block')

    def __init__(self, driver) -> None:
        """
        Инициализирует объект CartPage.

        Args:
            driver: Объект WebDriver.

        Returns:
            None
        """
        self.driver = driver
    def open(self) -> None:
        """
        Открывает страницу корзины.

        Returns:
            None
        """

        self.driver.get(f'{config.BASE_URL}/cart')

    def has_item(self) -> bool:
        """
        Проверяет, есть ли товары в корзине.

        Returns:
            bool: True, если товар присутствует.
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CART_ITEM))
            return True
        except Exception:
            return False

    def proceed_to_checkout(self) -> None:
        """
        Переходит к оформлению заказа.

        Returns:
            None
        """
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()
