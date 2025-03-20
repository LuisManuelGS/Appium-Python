
class SwipeUtility:
    def __init__(self, driver):
        self.driver = driver

        self.swipe_start_x = 780
        self.swipe_start_y = 1000
        self.swipe_end_x = 780
        self.swipe_end_y = 500
        self.default_swipe_duration = 800  # Default duration in milliseconds

    def swipe_action(self, swipe_duration=None, swipe_start_x=None, swipe_start_y=None, swipe_end_x=None,
                     swipe_end_y=None):

        # Use the class variables or provided arguments for the swipe coordinates and duration
        swipe_duration = swipe_duration or self.default_swipe_duration
        swipe_start_x = swipe_start_x or self.swipe_start_x
        swipe_start_y = swipe_start_y or self.swipe_start_y
        swipe_end_x = swipe_end_x or self.swipe_end_x
        swipe_end_y = swipe_end_y or self.swipe_end_y
        # Calculate the distance in X and Y directions
        distance_x = swipe_end_x - swipe_start_x
        distance_y = swipe_end_y - swipe_start_y
        # Calculate the time per pixel (in milliseconds per pixel)
        time_per_pixel = swipe_duration / max(abs(distance_x), abs(distance_y))  # milliseconds per pixel
        # Perform the swipe by dividing the swipe duration across the distance
        self.driver.swipe(swipe_start_x, swipe_start_y, swipe_end_x, swipe_end_y, swipe_duration)

        print(f"Swipe performed with a duration of {swipe_duration}ms.")
        print(f"Swipe speed: {1 / time_per_pixel:.2f} pixels/ms")