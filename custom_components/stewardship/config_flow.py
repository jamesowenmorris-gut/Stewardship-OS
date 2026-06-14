from homeassistant import config_entries
import voluptuous as vol

# The domain must match the one defined in your manifest.json
DOMAIN = "stewardship"

class StewardshipConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Stewardship OS."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step when the user adds the integration."""
        errors = {}

        if user_input is not None:
            # You could add validation logic here (e.g., checking if the Node ID is unique)
            return self.async_create_entry(
                title=f"Stewardship Node: {user_input['node_id']}", 
                data=user_input
            )

        # The form shown to the user
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("node_id", default="NODE-001"): str,
                vol.Required("location", default="Cardiff"): str,
            }),
            errors=errors,
        )
