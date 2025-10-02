from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class CheckoutPage:
    """
    Page Object для страницы оформления заказа на chitai-gorod.ru.
    """
    DELIVERY_METHOD_COURIER = (By.CLASS_NAME, "delivery-type__button chg-app-button chg-app-button--primary chg-app-button--xl chg-app-button--breeze chg-app-button--block delivery-type__block delivery-type__block--active") 
    STREET_FIELD = (By.name, "fullAddress")  # Поле "Улица и номер дома" 
    APARTMENT_FIELD = (By.name, "flat")  # Поле "Квартира"
    DELIVERY_SERVICE_SELECT = (By.CLASS_NAME, "radiobutton-native courier-item__mark radiobutton-native--active")  # Выбор службы доставки 
    PAYMENT_UPON_RECEIPT = (By.CLASS_NAME, "payments-item payments__item payments-item--active]")  # "при получении"
    FIO_FIELD = (By.name, "name")  # Поле ФИО
    EMAIL_FIELD = (By.name, "email")  # Поле email
    PHONE_FIELD = (By.name, "phone")  # Поле телефон
    SUBMIT_ORDER_BUTTON = (By.CLASS_NAME, "checkout-summary__button chg-app-button chg-app-button--primary chg-app-button--m chg-app-button--breeze")  # Кнопка "Оформить заказ" 

    def __init__(self, driver) -> None:
        """
        Инициализирует объект CheckoutPage с драйвером Selenium.

        Args:
            driver: Объект WebDriver для управления браузером.

        Returns:
            None
        """
        self.driver = driver

    def select_delivery_method_courier(self) -> None:
        """
        Выбирает способ получения "курьером".

        Returns:
            None
        """
        courier_radio = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DELIVERY_METHOD_COURIER)
        )
        courier_radio.click()

    def fill_address(self, street: str, apartment: str) -> None:
        """
        Заполняет поля адреса: улица и номер дома, квартира.

        Args:
            street (str): Улица и номер дома.
            apartment (str): Номер квартиры.

        Returns:
            None
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.STREET_FIELD)).send_keys(street)
        self.driver.find_element(*self.APARTMENT_FIELD).send_keys(apartment)

    def select_delivery_service(self, service_option: str) -> None:
        """
        Выбирает службу доставки.

        Args:
            service_option (str): Значение опции службы доставки (например, текст или value).

        Returns:
            None
        """
        delivery_select = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DELIVERY_SERVICE_SELECT)
        ))
        delivery_select.select_by_visible_text(service_option) 

    def select_payment_upon_receipt(self) -> None:
        """
        Выбирает способ оплаты "при получении".

        Returns:
            None
        """
        payment_radio = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PAYMENT_UPON_RECEIPT)
        )
        payment_radio.click()

    def fill_recipient_details(self, fio: str, email: str, phone: str) -> None:
        """
        Заполняет данные получателя: ФИО, email, телефон.

        Args:
            fio (str): ФИО получателя.
            email (str): Email.
            phone (str): Телефон.

        Returns:
            None
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FIO_FIELD)).send_keys(fio)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)

    def submit_order(self) -> None:
        """
        Нажимает кнопку "Оформить заказ".

        Returns:
            None
        """
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_ORDER_BUTTON)
        )
        submit_button.click()

    def is_form_visible(self) -> bool:
        """
        Проверяет, видна ли форма оформления.

        Returns:
            bool: True, если форма присутствует.
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SUBMIT_ORDER_BUTTON))
            return True
        except Exception:
            return False
