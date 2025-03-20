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
    swipe_utility.swipe_action(swipe_duration=100)
    set_timer.clickSetCount()
    set_timer.clickStartBtn()

    notification_text = notification.getNotification()
    assert "Countdown finished" == notification_text, f"Alert text does not match. Found: {notification_text}"

    driver.press_keycode(4)
    driver.quit()