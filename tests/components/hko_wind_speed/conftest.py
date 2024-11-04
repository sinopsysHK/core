"""Configure py.test."""

from unittest.mock import patch

import pytest

from tests.common import load_fixture


@pytest.fixture(name="hkows_config_flow_connect", autouse=True)
def hkows_config_flow_connect():
    """Mock valid config flow setup."""
    with patch(
        "homeassistant.components.hko_wind_speed.config_flow.HKOWS.wind",
        return_value=load_fixture("hko_wind_speed/latest_10min_wind.csv"),
    ):
        yield
