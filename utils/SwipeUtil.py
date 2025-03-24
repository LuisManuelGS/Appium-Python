import time

from utils.SettingsTestData import SettingsTestData

class SwipeUtility:
    def __init__(self, driver):
        self.driver = driver


    def swipe_up_one_second(self, start_x=None, start_y=None, height=None, duration=300):

        """
        Swipe up on the time picker to increase the timer by one second.

        :param start_x: Starting X coordinate (center of the picker)
        :param start_y: Starting Y coordinate (starting position)
        :param height: Height of the picker (determines the swipe distance)
        :param duration: Swipe duration in milliseconds
        """
        start_x = start_x or SettingsTestData.get_picker_coordinates().MIDPOINT_ON_X #(location in x = 658 + width = 236 // 2) Midpoint on X
        start_y = start_y or SettingsTestData.get_picker_coordinates().STARTING_POINT_ON_Y #(location in y = 830 + height = 603 // 4) Starting point on the picker
        height = height or SettingsTestData.get_picker_coordinates().SWIPE_PER_SECOND #(height = 603 // 6) Swipes a segment (approximately one second)

        end_y = start_y - height

        # Swipe up
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        time.sleep(0.7) # Waits 700ms to ensure the change is registered

        print(f"Swipe made of {start_y} to {end_y} in {duration}ms.")