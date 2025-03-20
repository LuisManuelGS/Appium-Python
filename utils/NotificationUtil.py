from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Notification:
    def __init__(self, driver):
        self.driver = driver

    def getNotification(self, timeout=10):
        # Open the notification panel
        self.driver.open_notifications()
        try:
            notification = WebDriverWait(self.driver, timeout).until(
                presence_of_element_located((AppiumBy.XPATH, '//*[@text="Countdown finished"]'))
            )
            return notification.text
        except Exception:
            return None