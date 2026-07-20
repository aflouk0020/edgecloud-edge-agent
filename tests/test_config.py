import os
import unittest
from unittest.mock import patch

from src.config import read_positive_int_environment


class ConfigurationTest(unittest.TestCase):

    def test_returns_default_when_variable_is_missing(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            result = read_positive_int_environment(
                "TELEMETRY_INTERVAL_SECONDS",
                5,
            )

        self.assertEqual(result, 5)

    def test_reads_positive_integer_environment_value(self) -> None:
        with patch.dict(
            os.environ,
            {"TELEMETRY_INTERVAL_SECONDS": "15"},
            clear=False,
        ):
            result = read_positive_int_environment(
                "TELEMETRY_INTERVAL_SECONDS",
                5,
            )

        self.assertEqual(result, 15)

    def test_rejects_zero_value(self) -> None:
        with patch.dict(
            os.environ,
            {"TELEMETRY_INTERVAL_SECONDS": "0"},
            clear=False,
        ):
            with self.assertRaisesRegex(
                ValueError,
                "must be greater than zero",
            ):
                read_positive_int_environment(
                    "TELEMETRY_INTERVAL_SECONDS",
                    5,
                )

    def test_rejects_negative_value(self) -> None:
        with patch.dict(
            os.environ,
            {"TELEMETRY_INTERVAL_SECONDS": "-10"},
            clear=False,
        ):
            with self.assertRaisesRegex(
                ValueError,
                "must be greater than zero",
            ):
                read_positive_int_environment(
                    "TELEMETRY_INTERVAL_SECONDS",
                    5,
                )

    def test_rejects_non_numeric_value(self) -> None:
        with patch.dict(
            os.environ,
            {"TELEMETRY_INTERVAL_SECONDS": "invalid"},
            clear=False,
        ):
            with self.assertRaisesRegex(
                ValueError,
                "must be a valid integer",
            ):
                read_positive_int_environment(
                    "TELEMETRY_INTERVAL_SECONDS",
                    5,
                )


if __name__ == "__main__":
    unittest.main()
