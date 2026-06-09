import os

DEVICE_ID = os.getenv("EDGE_DEVICE_ID", "simulated-edge-device-01")

MONITORING_SERVICE_URL = os.getenv(
    "MONITORING_SERVICE_URL",
    "http://localhost:8082/telemetry"
)

SIMULATION_MODE = os.getenv("SIMULATION_MODE", "true").lower() == "true"

REQUEST_TIMEOUT_SECONDS = int(os.getenv("REQUEST_TIMEOUT_SECONDS", "10"))

TELEMETRY_INTERVAL_SECONDS = int(os.getenv("TELEMETRY_INTERVAL_SECONDS", "5"))
