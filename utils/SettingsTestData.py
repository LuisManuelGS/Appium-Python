import json
import logging
import os
from typing import Optional
from model.WaitData import WaitData


class SettingsTestData:

    PATH = os.path.join(os.path.dirname(__file__), '..', 'resources', 'settings.json')
    ERROR_MSG = "File with wait settings not found or incorrect"

    @staticmethod
    def get_wait_data() -> Optional[WaitData]:
        try:
            with open(SettingsTestData.PATH, "r") as file:
                data = json.load(file)
                return WaitData(**data)
        except FileNotFoundError:
            logging.error(SettingsTestData.ERROR_MSG)
            raise RuntimeError(SettingsTestData.ERROR_MSG)
        except json.JSONDecodeError:
            logging.error("JSON is invalid or could not be decoded.")
            raise RuntimeError("JSON is invalid or could not be decoded.")
