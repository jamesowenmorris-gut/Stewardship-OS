import logging
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

class StewardshipCoordinator(DataUpdateCoordinator):
    """The central brain of the Stewardship OS."""

    def __init__(self, hass: HomeAssistant, config_entry):
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name="Stewardship OS",
            update_interval=timedelta(seconds=30),  # Polling interval
        )
        self.config_entry = config_entry

    async def _async_update_data(self):
        """Fetch data from sensors and apply Constitution logic."""
        try:
            # 1. Fetch current sensor values 
            # (Replace these with real entity_id lookups later)
            grid_usage = self.hass.states.get("sensor.grid_power")
            solar_gen = self.hass.states.get("sensor.solar_power")
            battery_level = self.hass.states.get("sensor.battery_level")

            # Default to 0 if sensors aren't ready yet
            usage = float(grid_usage.state) if grid_usage else 0
            solar = float(solar_gen.state) if solar_gen else 0
            battery = float(battery_level.state) if battery_level else 100

            # 2. Run the Constitution Logic
            decision = self._apply_constitution(usage, solar, battery)
            
            return {
                "grid_usage": usage,
                "solar_gen": solar,
                "battery_level": battery,
                "node_state": decision
            }
        except Exception as err:
            raise UpdateFailed(f"Error communicating with hardware: {err}")

    def _apply_constitution(self, usage, solar, battery):
        """
        The Logic Engine: The interpretation of the Constitution.
        """
        # RULE 1: VITALITY (If grid is gone and battery low, shed load)
        if battery < 20:
            return "VITALITY_CRITICAL"

        # RULE 2: RESILIENCE (If we have power, we maintain the island)
        if solar > usage:
            return "MESH_RECIPROCITY" # We have surplus to share
            
        # RULE 3: STABILITY (Standard operation)
        return "STABLE_GRID"
