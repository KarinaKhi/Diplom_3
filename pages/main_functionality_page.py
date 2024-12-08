from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_functionality_locators import MainFunctionalityPageLocators
from pages.base_page import BasePage


class ValidCreateOrderRender(object):
    def __init__(self, locator, text="9999"):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if element.text != self.text:
            return element
        else:
            return False


class MainFunctionalityPage(BasePage):
    def click_on_constructor_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(MainFunctionalityPageLocators.OVERLAYER_FOR_ORDERS)
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(MainFunctionalityPageLocators.CONSTRUCTOR_BUTTON))
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(MainFunctionalityPageLocators.CONSTRUCTOR_BUTTON))
        self.click_element(MainFunctionalityPageLocators.CONSTRUCTOR_BUTTON)

    def click_on_order_feed_button(self):
        self.scroll_into_view(MainFunctionalityPageLocators.ORDER_FEED)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(MainFunctionalityPageLocators.ORDER_FEED))
        self.click_element(MainFunctionalityPageLocators.ORDER_FEED)

    def click_on_ingredient(self, ingredient_locator):
        self.click_element(ingredient_locator)

    def click_on_order_button(self):
        self.click_element(MainFunctionalityPageLocators.ORDER_BUTTON)

    def get_created_orger_number(self):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(MainFunctionalityPageLocators.OVERLAYER_FOR_ORDERS)
        )

        counter = WebDriverWait(self.driver, 20).until(
            ValidCreateOrderRender(MainFunctionalityPageLocators.CREATED_ORDER_NUMBER)
        )
        return counter.text

    def close_modal_window(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainFunctionalityPageLocators.CROSS_BUTTON))
        self.click_element(MainFunctionalityPageLocators.CROSS_BUTTON)

    def is_ingredient_counter_updated(self, counter_locator):
        try:
            counter = self.find_element(counter_locator)
            return int(counter.text) > 0
        except TimeoutException:
            return False

    def add_ingredient_to_order(self, ingredient_locator):
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ingredient_locator)
        )
        self.scroll_into_view(ingredient_locator)
        order_constructor = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainFunctionalityPageLocators.ORDER_CONSTRUCTOR)
        )
        self.scroll_into_view(MainFunctionalityPageLocators.ORDER_CONSTRUCTOR)

        drag_drop_script = """
        function createEvent(typeOfEvent) {
            var event = document.createEvent("CustomEvent");
            event.initCustomEvent(typeOfEvent, true, true, null);
            event.dataTransfer = {
                data: {},
                setData: function(key, value) {
                    this.data[key] = value;
                },
                getData: function(key) {
                    return this.data[key];
                }
            };
            return event;
        }

        function dispatchEvent(element, event, transferData) {
            if (transferData !== undefined) {
                event.dataTransfer = transferData;
            }
            if (element.dispatchEvent) {
                element.dispatchEvent(event);
            } else if (element.fireEvent) {
                element.fireEvent("on" + event.type, event);
            }
        }

        function simulateDragAndDrop(source, target) {
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(source, dragStartEvent);

            var dropEvent = createEvent('drop');
            dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);

            var dragEndEvent = createEvent('dragend');
            dispatchEvent(source, dragEndEvent, dropEvent.dataTransfer);
        }

        simulateDragAndDrop(arguments[0], arguments[1]);
        """

        self.driver.execute_script(drag_drop_script, ingredient, order_constructor)

    def is_modal_window_closed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(MainFunctionalityPageLocators.MODAL_WINDOW)
            )
            return True
        except TimeoutException:
            return False
