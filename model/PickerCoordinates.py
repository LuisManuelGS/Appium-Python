from dataclasses import dataclass

@dataclass
class PickerCoordinates:
    MIDPOINT_ON_X: int
    STARTING_POINT_ON_Y: int
    SWIPE_PER_SECOND: int