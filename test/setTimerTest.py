from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from base.DriverClass import Driver
from base.BasePage import BasePage


def test_count_down():
    driver1 = Driver()
    driver = driver1.getDriverMethod()

    bp = BasePage(driver)
    element = bp.waitForElement("android:id/button1","id")
    element.click()

    allow_notification = bp.waitForElement("com.android.permissioncontroller:id/permission_allow_button", "id")
    allow_notification.click()

    for i in range(3):
        ok_got_it_btn = bp.waitForElement("com.sportstracklive.stopwatch:id/dismiss_button", "id")
        ok_got_it_btn.click()

    count_down = bp.waitForElement("com.sportstracklive.stopwatch:id/countDown", "id")
    count_down.click()

    frame_layout = bp.waitForElement('new UiSelector().className("android.widget.FrameLayout").instance(0)',"uiautomator")
    if frame_layout.is_displayed():
        print("\nFrameLayout found and visible.")
    else:
        print("\nFrameLayout not found.")

    driver.swipe(780, 1000, 780, 500, 800)

    set_count = bp.waitForElement("com.sportstracklive.stopwatch:id/setCountDown", "id")
    set_count.click()

    start = bp.waitForElement("com.sportstracklive.stopwatch:id/start","id")
    start.click()

    # Open the notification panel
    driver.open_notifications()

    notification = WebDriverWait(driver, 10).until(
                 presence_of_element_located((AppiumBy.XPATH, '//*[@text="Countdown finished"]')))

    notification_text = notification.text

    assert "Countdown finished" == notification_text, f"Alert text does not match. Found: {notification_text}"

    driver.press_keycode(4)
    driver.quit()




