from homeassistant.components.switch import SwitchEntity
from .coordinator import StewardshipCoordinator

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Stewardship switches."""
    coordinator = hass.data["stewardship"][entry.entry_id]
    async_add_entities([StewardshipLoadSheddingSwitch(coordinator)])

class StewardshipLoadSheddingSwitch(SwitchEntity):
    """A switch that allows manual or automatic shedding of non-essential loads."""
    
    def __init__(self, coordinator: StewardshipCoordinator):
        self.coordinator = coordinator
        self._state = False

    @property
    def name(self):
        return "Stewardship Load Shedder"

    @property
    def is_on(self):
        # The switch is 'on' if the Constitution has triggered load shedding
        return self.coordinator.data.get("node_state") == "CONSERVATION_MODE"

    async def async_turn_on(self, **kwargs):
        """Logic to force load shedding."""
        # You would add your API call here to your physical Shelly/Relay
        self._state = True
        self.schedule_update_ha_state()

    async def async_turn_off(self, **kwargs):
        """Logic to restore power."""
        self._state = False
        self.schedule_update_ha_state()
