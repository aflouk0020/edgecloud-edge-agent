import os


def read_positive_int_environment(
    variable_name: str,
    default_value: int,
) -> int:
    raw_value = os.getenv(variable_name, str(default_value))

    try:
        parsed_value = int(raw_value)
    except ValueError as exc:
        raise ValueError(
            f"{variable_name} must be a valid integer, "
            f"but received: {raw_value!r}"
        ) from exc

    if parsed_value <= 0:
        raise ValueError(
            f"{variable_name} must be greater than zero, "
            f"but received: {parsed_value}"
        )

    return parsed_value


DEVICE_ID = os.getenv(
    "EDGE_DEVICE_ID",
    "simulated-edge-device-01",
)

MONITORING_SERVICE_URL = os.getenv(
    "MONITORING_SERVICE_URL",
    "http://localhost:8082/telemetry",
)

DEVICE_SERVICE_URL = os.getenv(
    "DEVICE_SERVICE_URL",
    "http://localhost:8083/heartbeat",
)

SIMULATION_MODE = (
    os.getenv("SIMULATION_MODE", "true").lower() == "true"
)

REQUEST_TIMEOUT_SECONDS = read_positive_int_environment(
    "REQUEST_TIMEOUT_SECONDS",
    10,
)

TELEMETRY_INTERVAL_SECONDS = read_positive_int_environment(
    "TELEMETRY_INTERVAL_SECONDS",
    5,
)
