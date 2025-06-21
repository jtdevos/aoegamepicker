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

        