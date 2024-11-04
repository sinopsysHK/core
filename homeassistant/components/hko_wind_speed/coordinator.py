"""Weather data coordinator for the HKO [Wind Speed] API."""

from asyncio import timeout
import csv
from datetime import timedelta
from io import StringIO
import logging
from typing import Any

from aiohttp import ClientSession

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import API_ENDPOINT, API_STATION, DOMAIN

_LOGGER = logging.getLogger(__name__)


class HKOWSError(Exception):
    """HKO Wind Speed error."""


class HKOWS:
    """HKO Wind Speed Connector."""

    def __init__(self, session: ClientSession) -> None:
        """Get data via HKO API."""
        self.session = session

    async def wind(self) -> str:
        """Retrieve data from HKO API."""
        async with self.session.get(API_ENDPOINT) as response:
            if response.status != 200:
                raise HKOWSError("Cannot connect to HKOWS API")
            try:
                content = await response.text()
            except Exception as e:
                raise HKOWSError(f"HKOWS API Error: {e}") from e
            return content


class HKOWSUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """HKO Wind Speed Update Coordinator."""

    def __init__(
        self, hass: HomeAssistant, session: ClientSession, location: str
    ) -> None:
        """Update data via library."""
        self.location = location
        self.websession = session
        self.hkows = HKOWS(session)

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=10),
        )

    async def _async_update_data(self) -> dict[str, Any]:
        """Update data via HKO library."""
        try:
            async with timeout(60):
                content = await self.hkows.wind()
        except HKOWSError as error:
            raise UpdateFailed(error) from error
        reader = csv.DictReader(StringIO(content))
        return next(item for item in reader if item[API_STATION] == self.location)
