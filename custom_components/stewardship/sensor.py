from homeassistant.components.sensor import SensorEntity
from .coordinator import StewardshipCoordinator

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Stewardship sensors."""
    coordinator = hass.data["stewardship"][entry.entry_id]
    
    # We add our sensor class here
    async_add_entities([StewardshipStateSensor(coordinator)])

class StewardshipStateSensor(SensorEntity):
    """A sensor that represents the current state of the Mesh."""

    def __init__(self, coordinator: StewardshipCoordinator):
        self.coordinator = coordinator
        # The unique ID ensures Home Assistant doesn't duplicate this sensor
        self._attr_unique_id = f"stewardship_state_{coordinator.config_entry.entry_id}"
        self._attr_name = "Stewardship Node State"
        self._attr_icon = "mdi:home-lightning-bolt"

    @property
    def state(self):
        """Returns the current operating mode of the node."""
        # This pulls directly from the dict we returned in coordinator.py
        return self.coordinator.data.get("node_state", "INITIALIZING")

    @property
    def available(self):
        """Return True if the coordinator has valid data."""
        return self.coordinator.last_update_success

    @property
    def extra_state_attributes(self):
        """Return extra data for the dashboard (e.g., usage/gen)."""
        return {
            "grid_usage": self.coordinator.data.get("grid_usage"),
            "solar_gen": self.coordinator.data.get("solar_gen"),
            "battery_level": self.coordinator.data.get("battery_level"),
        }
