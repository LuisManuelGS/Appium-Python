from appium import  webdriver
from appium.options.android import UiAutomator2Options

class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '15'
        desired_caps['deviceName'] = 'Medium Phone API 35'
        desired_caps['app'] = '/Users/l.garcia/PycharmProjects/AppiumPythonTask/resources/stopwatch-andamp-timer-1-54.apk'
        desired_caps['appPackage'] = 'com.sportstracklive.stopwatch'
        desired_caps['appActivity'] = 'com.sportstracklive.stopwatch.StandardStopWatchActivity'

        options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)

        return driver

