# EdgeCloud Edge Agent

The EdgeCloud Edge Agent is a Python-based telemetry client used to collect system metrics from a Raspberry Pi or simulated edge device and transmit them to the EdgeCloud Monitor platform.

## Responsibilities

The agent:

- collects CPU, memory and temperature telemetry
- submits telemetry to the Monitoring Service
- sends device heartbeats to the Device Service
- supports simulated and Raspberry Pi environments
- uses environment-based configuration
- validates timing configuration during startup

## Configuration

The following environment variables are supported:

| Variable | Default | Description |
|---|---:|---|
| `EDGE_DEVICE_ID` | `simulated-edge-device-01` | Unique edge-device identifier |
| `MONITORING_SERVICE_URL` | `http://localhost:8082/telemetry` | Monitoring Service telemetry endpoint |
| `DEVICE_SERVICE_URL` | `http://localhost:8083/heartbeat` | Device Service heartbeat endpoint |
| `SIMULATION_MODE` | `true` | Enables simulated telemetry collection |
| `REQUEST_TIMEOUT_SECONDS` | `10` | HTTP request timeout in seconds |
| `TELEMETRY_INTERVAL_SECONDS` | `5` | Delay between telemetry collection cycles |

`REQUEST_TIMEOUT_SECONDS` and `TELEMETRY_INTERVAL_SECONDS` must contain positive integer values.

The agent stops during configuration loading with a clear error if either value is zero, negative or non-numeric.

## Local Configuration

Create a local environment file from the supplied example:

    cp .env.example .env

Environment variables may also be exported directly:

    export TELEMETRY_INTERVAL_SECONDS=15
    export REQUEST_TIMEOUT_SECONDS=10

## Running the Agent

Install dependencies:

    python3 -m pip install -r requirements.txt

Start the agent:

    python3 main.py

## Running Tests

Run the configuration tests using Python's standard `unittest` framework:

    python3 -m unittest discover -s tests -v
