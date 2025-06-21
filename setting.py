class Setting:
    def __init__(self, name, options):
        """
Initialize a new Setting.

:param name: str - The name of the setting (e.g., "Game Mode")
:param options: iterable - A list, set, or tuple of available options
        """
        self.name = name
        self.options = set(options)

    def add_option(self, option):
        """Add a new option to the setting."""
        self.options.add(option)

    def remove_option(self, option):
        """Remove an option from the setting if it exists."""
        self.options.discard(option)

    def has_option(self, option):
        """Check if the setting includes a specific option."""
        return option in self.options

    def __repr__(self):
        return f"Setting(name='{self.name}', options={sorted(self.options)})"


class BooleanSetting(Setting):
    def __init__(self, name, enabled=False):
        """
Initialize a BooleanSetting.

:param name: str - The name of the setting (e.g., "Cheats Enabled")
:param enabled: bool - Whether the setting is enabled
        """
        super().__init__(name, options=[True, False])
        self.enabled = enabled

    def toggle(self):
        """Toggle the enabled state."""
        self.enabled = not self.enabled

    def __repr__(self):
        return f"BooleanSetting(name='{self.name}', enabled={self.enabled})"

class SettingGroup:
    def __init__(self, name, settings=None):
        """
        Initialize a SettingGroup.

        :param name: str - The name of the group (e.g., "Game Settings")
        :param settings: list of Setting - Optional initial list of settings
        """
        self.name = name
        self.settings = list(settings) if settings else []

    def add_setting(self, setting):
        """Add a Setting object to the group."""
        if not isinstance(setting, Setting):
            raise TypeError("Only Setting instances can be added")
        self.settings.append(setting)

    def get_setting(self, name):
        """Retrieve a Setting by name (first match), or None if not found."""
        for setting in self.settings:
            if setting.name == name:
                return setting
        return None

    def remove_setting(self, name):
        """Remove the first Setting with the given name."""
        self.settings = [s for s in self.settings if s.name != name]

    def list_settings(self):
        """Return the list of settings in the group."""
        return self.settings

    def __repr__(self):
        names = [s.name for s in self.settings]
        return f"SettingGroup(name='{self.name}', settings={names})"


# --- Aliases ---
S = Setting
BS = BooleanSetting
SG = SettingGroup
# Public API
__all__ = ["Setting", "BooleanSetting", "SettingGroup", "S", "BS", "SG"]
