
from base.DriverClass import Driver
from pages.setTimerPage import SetTimer
from utils.NotificationUtil import Notification
from utils.SwipeUtil import SwipeUtility


def test_count_down():

    driver1 = Driver()
    driver = driver1.getDriverMethod()

    set_timer = SetTimer(driver)
    swipe_utility = SwipeUtility(driver)
    notification = Notification(driver)

    set_timer.clickPermissionsButton()
    set_timer.clickAllowNoifications()
    set_timer.clickGotItBtn()
    set_timer.clickCountDownBtn()
    assert set_timer.isFrameDisplayed(), "FrameLayout not found."

    set_timer.coordinates()
    for _ in range(5):  # Scroll down the number of times indicated in range.
        swipe_utility.swipe_up_one_second()

    set_timer.clickSetCount()
    set_timer.clickStartBtn()

    notification_text = notification.getNotification(6)
    assert "Countdown finished" == notification_text, f"Alert text does not match. Found: {notification_text}"

    driver.press_keycode(4)
    driver.quit()