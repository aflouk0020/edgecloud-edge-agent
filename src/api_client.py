import logging

import requests

from src.config import MONITORING_SERVICE_URL, REQUEST_TIMEOUT_SECONDS


class MonitoringApiClient:
    def send_telemetry(self, payload: dict) -> bool:
        try:
            response = requests.post(
                MONITORING_SERVICE_URL,
                json=payload,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )

            logging.info("Telemetry POST status: %s", response.status_code)

            if response.status_code in (200, 201, 202):
                return True

            logging.warning("Telemetry submission failed: %s", response.text)
            return False

        except requests.RequestException as exc:
            logging.error("Telemetry submission error: %s", exc)
            return False
