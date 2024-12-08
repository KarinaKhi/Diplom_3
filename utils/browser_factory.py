from selenium import webdriver


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name.lower() == "firefox":
            return webdriver.Firefox()
        elif browser_name.lower() == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Неподдерживаемый браузер: {browser_name}")
