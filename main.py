import logging
import time

from src.api_client import MonitoringApiClient
from src.config import TELEMETRY_INTERVAL_SECONDS
from src.telemetry_collector import TelemetryCollector


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def run_once(collector: TelemetryCollector, client: MonitoringApiClient) -> None:
    payload = collector.collect()
    logging.info("Collected telemetry payload: %s", payload)

    submitted = client.send_telemetry(payload)

    if submitted:
        logging.info("Telemetry submitted successfully")
    else:
        logging.warning("Telemetry was collected but not submitted successfully")


def main() -> None:
    configure_logging()

    collector = TelemetryCollector()
    client = MonitoringApiClient()

    logging.info("Starting Edge Telemetry Agent")
    logging.info("Telemetry interval: %s seconds", TELEMETRY_INTERVAL_SECONDS)

    try:
        while True:
            run_once(collector, client)
            logging.info("Waiting %s seconds before next collection", TELEMETRY_INTERVAL_SECONDS)
            time.sleep(TELEMETRY_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        logging.info("Edge Telemetry Agent stopped manually")


if __name__ == "__main__":
    main()
