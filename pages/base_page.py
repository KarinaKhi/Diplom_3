from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.main_functionality_locators import MainFunctionalityPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_driver = WebDriverWait(self.driver, 20)

    def scroll_to_element(self, element):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_element(self, locator):
        try:
            self.wait_driver.until(
                EC.invisibility_of_element_located(MainFunctionalityPageLocators.OVERLAYER_FOR_ORDERS)
            )
            self.wait_driver.until(EC.visibility_of_element_located(locator))
            self.wait_driver.until(EC.presence_of_element_located(locator))
            self.wait_driver.until(EC.visibility_of_all_elements_located(locator))
            element = self.wait_driver.until(EC.element_to_be_clickable(locator))
            self.scroll_to_element(element)
            element.click()
        except TimeoutException:
            print(f"Элемент с локатором {locator} не найден или не кликабелен.")

    def find_element(self, locator):
        return self.wait_driver.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_be_visible(self, element_or_locator, timeout=10):
        if isinstance(element_or_locator, tuple):
            return self.wait_driver.until(
                EC.visibility_of_element_located(element_or_locator)
            )
        else:
            return self.wait_driver.until(
                EC.visibility_of(element_or_locator)
            )

    def wait_for_element_to_be_clickable(self, locator):
        self.wait_driver.until(
            EC.element_to_be_clickable(locator)
        )

    def set_page_zoom(self, zoom_level=1.0):
        self.driver.execute_script(f"document.body.style.zoom='{zoom_level}'")

    def scroll_into_view(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
