import logging

from src.api_client import MonitoringApiClient
from src.telemetry_collector import TelemetryCollector


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def main() -> None:
    configure_logging()

    collector = TelemetryCollector()
    client = MonitoringApiClient()

    payload = collector.collect()
    logging.info("Collected telemetry payload: %s", payload)

    submitted = client.send_telemetry(payload)

    if submitted:
        logging.info("Telemetry submitted successfully")
    else:
        logging.warning("Telemetry was collected but not submitted successfully")


if __name__ == "__main__":
    main()
