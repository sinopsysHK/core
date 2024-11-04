"""Support for the HKO Wind Speed service."""

from homeassistant.components.weather import WeatherEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfSpeed
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    API_BEARING,
    API_GUST_SPEED,
    API_WIND_SPEED,
    ATTRIBUTION,
    CARDINAL_DIRECTIONS,
    DOMAIN,
    MANUFACTURER,
)
from .coordinator import HKOWSUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Add a HKOWS weather entity from a config_entry."""
    assert config_entry.unique_id is not None
    unique_id = config_entry.unique_id
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([HKOWSEntity(unique_id, coordinator)], False)


class HKOWSEntity(CoordinatorEntity[HKOWSUpdateCoordinator], WeatherEntity):
    """Define a HKOWS entity."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_native_windspeed_unit = UnitOfSpeed.KILOMETERS_PER_HOUR
    _attr_attribution = ATTRIBUTION

    def __init__(self, unique_id: str, coordinator: HKOWSUpdateCoordinator) -> None:
        """Initialise the weather platform."""
        super().__init__(coordinator)
        self._attr_unique_id = unique_id
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, unique_id)},
            manufacturer=MANUFACTURER,
            entry_type=DeviceEntryType.SERVICE,
        )

    @property
    def native_wind_gust_speed(self) -> float | None:
        """Return the wind gust speed in native units."""
        return self.coordinator.data[API_GUST_SPEED]

    @property
    def native_wind_speed(self) -> float | None:
        """Return the wind speed in native units."""
        return self.coordinator.data[API_WIND_SPEED]

    @property
    def wind_bearing(self) -> float | str | None:
        """Return the wind bearing."""
        return _cardinal_to_degrees(self.coordinator.data[API_BEARING])


def _cardinal_to_degrees(value: str | float | None) -> int | float | None:
    """Translate a cardinal direction into azimuth angle (degrees)."""
    if not isinstance(value, str):
        return value

    try:
        return float(360 / 16 * CARDINAL_DIRECTIONS.index(value))
    except ValueError:
        return None
