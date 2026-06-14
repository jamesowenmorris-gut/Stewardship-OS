"""The Stewardship OS integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .coordinator import StewardshipCoordinator

# Define the platforms your integration supports
# This tells Home Assistant to look for sensor.py and switch.py
PLATFORMS: list[Platform] = [Platform.SENSOR, Platform.SWITCH]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Stewardship OS from a config entry."""
    
    # Initialize the Coordinator
    coordinator = StewardshipCoordinator(hass, entry)
    
    # Fetch initial data to ensure the integration starts with valid state
    await coordinator.async_config_entry_first_refresh()

    # Store the coordinator in hass.data so other platforms can access it
    hass.data.setdefault("stewardship", {})
    hass.data["stewardship"][entry.entry_id] = coordinator

    # Forward the setup to the platforms defined in the PLATFORMS list
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    
    # Unload the platforms safely
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
    # Clean up the data store
    if unload_ok:
        hass.data["stewardship"].pop(entry.entry_id)
        
    return unload_ok
