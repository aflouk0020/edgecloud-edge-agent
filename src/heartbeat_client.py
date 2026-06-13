import logging
from datetime import datetime

import requests

from src.config import (
    DEVICE_ID,
    DEVICE_SERVICE_URL,
    REQUEST_TIMEOUT_SECONDS
)


class HeartbeatClient:

    def send_heartbeat(self) -> bool:

        payload = {
            "deviceId": DEVICE_ID,
            "timestamp": datetime.now().isoformat()
        }

        try:
            response = requests.post(
                DEVICE_SERVICE_URL,
                json=payload,
                timeout=REQUEST_TIMEOUT_SECONDS
            )

            logging.info(
                "Heartbeat POST status: %s",
                response.status_code
            )

            if response.ok:
                logging.info(
                    "Heartbeat submitted successfully"
                )
                return True

            logging.warning(
                "Heartbeat submission failed: %s",
                response.text
            )

            return False

        except Exception as ex:
            logging.error(
                "Heartbeat submission error: %s",
                ex
            )
            return False
