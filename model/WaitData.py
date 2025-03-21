from dataclasses import dataclass


@dataclass
class WaitData:
    WAIT_TIMEOUT: int
    POLL_FREQUENCY: float