#!/bin/bash

# Ensure directory exists
mkdir -p custom_components/stewardship

echo "Initializing Stewardship OS integration files..."

# 1. manifest.json
cat <<EOF > custom_components/stewardship/manifest.json
{
  "domain": "stewardship",
  "name": "Stewardship OS",
  "codeowners": ["@your_github_username"],
  "config_flow": true,
  "documentation": "https://github.com/your_username/stewardship-os",
  "iot_class": "local_push",
  "version": "1.0.0",
  "requirements": ["paho-mqtt==2.1.0"]
}
EOF

# 2. __init__.py
cat <<EOF > custom_components/stewardship/__init__.py
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .coordinator import StewardshipCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    coordinator = StewardshipCoordinator(hass, entry)
    hass.data.setdefault("stewardship", {})
    hass.data["stewardship"][entry.entry_id] = coordinator
    await coordinator.async_config_entry_first_refresh()
    await hass.config_entries.async_forward_entry_setup(entry, "sensor")
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
EOF

# 3. coordinator.py
cat <<EOF > custom_components/stewardship/coordinator.py
import logging
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from datetime import timedelta

_LOGGER = logging.getLogger(__name__)

class StewardshipCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, config_entry):
        super().__init__(hass, _LOGGER, name="Stewardship OS", update_interval=timedelta(seconds=30))

    async def _async_update_data(self):
        return {"node_state": "STABLE"}
EOF

# 4. sensor.py
cat <<EOF > custom_components/stewardship/sensor.py
from homeassistant.components.sensor import SensorEntity

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["stewardship"][entry.entry_id]
    async_add_entities([StewardshipStateSensor(coordinator)])

class StewardshipStateSensor(SensorEntity):
    def __init__(self, coordinator):
        self.coordinator = coordinator
    @property
    def name(self): return "Stewardship Node State"
    @property
    def state(self): return self.coordinator.data.get("node_state")
EOF

# 5. config_flow.py
cat <<EOF > custom_components/stewardship/config_flow.py
from homeassistant import config_entries
import voluptuous as vol

class StewardshipConfigFlow(config_entries.ConfigFlow, domain="stewardship"):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Stewardship Node", data=user_input)
        return self.async_show_form(step_id="user", data_schema=vol.Schema({vol.Required("node_id"): str}))
EOF

echo "Done. Stewardship OS structure initialized."
