import random

import psutil

from src.config import DEVICE_ID, SIMULATION_MODE


class TelemetryCollector:
    def collect(self) -> dict:
        return {
            "deviceId": DEVICE_ID,
            "cpuUsage": self._collect_cpu_usage(),
            "memoryUsage": self._collect_memory_usage(),
            "temperature": self._collect_temperature(),
        }

    def _collect_cpu_usage(self) -> float:
        if SIMULATION_MODE:
            return round(random.uniform(10.0, 85.0), 2)

        return round(psutil.cpu_percent(interval=1), 2)

    def _collect_memory_usage(self) -> float:
        if SIMULATION_MODE:
            return round(random.uniform(20.0, 90.0), 2)

        return round(psutil.virtual_memory().percent, 2)

    def _collect_temperature(self) -> float:
        if SIMULATION_MODE:
            return round(random.uniform(35.0, 75.0), 2)

        temperatures = getattr(psutil, "sensors_temperatures", lambda: {})()

        if not temperatures:
            return 0.0

        for entries in temperatures.values():
            if entries:
                return round(entries[0].current, 2)

        return 0.0
