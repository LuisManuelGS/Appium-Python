from utils.WaitUtil import WaitUtil

class SetTimer(WaitUtil):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _permissions = "android:id/button1"
    _allow_notification = "com.android.permissioncontroller:id/permission_allow_button"
    _ok_got_it = "com.sportstracklive.stopwatch:id/dismiss_button"
    _count_down = "com.sportstracklive.stopwatch:id/countDown"
    _frame_layout = 'new UiSelector().className("android.widget.FrameLayout").instance(0)'
    _set_count = "com.sportstracklive.stopwatch:id/setCountDown"
    _start = "com.sportstracklive.stopwatch:id/start"

    def clickPermissionsButton(self):
        permissions_btn = self.waitForElement(self._permissions,"id")
        permissions_btn.click()

    def clickAllowNoifications(self):
        allow_notification_btn = self.waitForElement(self._allow_notification,"id")
        allow_notification_btn.click()

    def clickGotItBtn(self):
        for i in range(3):
            ok_got_it_btn = self.waitForElement(self._ok_got_it,"id")
            ok_got_it_btn.click()

    def clickCountDownBtn(self):
        count_down_btn = self.waitForElement(self._count_down,"id")
        count_down_btn.click()

    def isFrameDisplayed(self):
        frame = self.waitForElement(self._frame_layout,"uiautomator")
        return frame.is_displayed()

    def clickSetCount(self):
        set_count = self.waitForElement(self._set_count,"id")
        set_count.click()

    def clickStartBtn(self):
        start_btn = self.waitForElement(self._start,"id")
        start_btn.click()