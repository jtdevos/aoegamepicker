from setting import S, BS, Setting
from typing import List

game_settings = (
    S('Data Mod', ('Definitive Set')),
    S('Game Mode', ("Random Map", "Empire Wars", "Death Match", "Regicide", "King of the Hill",
                    "Capture the Relic", "Wonder Race", "Defend the Wonder", "Sudden Death", "Battle Royale",
                    "Co-Op Campaign", "Custom Scenario")),
    S('Map Size',
      ('Tiny', 'Small', 'Medium', 'Normal', 'Large', 'Huge', 'Ludicrous')),
    S('AI Difficulty', ('Easiest', 'Standard', 'Moderate', 'Hard', 'Hardest', 'Extreme')),
    S('Resources', ('Standard', 'Low', 'Medium', 'High', 'Ultra High', 'Infinite', 'Ultra High', 'Infinite', 'Random')),
    S('Population', tuple([x for x in range(25, 501, 25)]) ),
    S('Game Speed', ('Slow', 'Casual', 'Normal', 'Fast')),
    S('Reveal Map', ('Normal', 'Explored', 'All Visible')),
    S('Starting Age', ('Standard', 'Dark Age', 'Feudal Age', 'Castle Age', 'Imperial Age', 'Post-Imperial Age')),
    S('Ending Age', ('Standard', 'Dark Age', 'Feudal Age', 'Castle Age', 'Imperial Age')),
    S('Treaty Length', tuple([f'{x} Minutes' for x in range(5, 91, 5)])),
    S('Victory', ('Standard', 'Conquest', 'Time Limit', 'Score', 'Last Man Standing')),
    S('Score', tuple([x for x in range(14000, 3999, -1000)]))
)

team_settings = (
    BS('Lock Teams'),
    BS('Team Together'),
    BS('Team Positions'),
    BS('Shared Exploration'),
    BS('Handicap')
    )

advanced_settings = (
    BS('Lock Speed'),
    BS('Allow Cheats'),
    BS('Turbo Mode'),
    BS('Full Tech Tree'),
    BS('Empire Wars Mode'),
    BS('Regicide Mode'),
    BS('Antiquity Mode'),
    BS('Record Game')
)

def get_setting(settings: List[Setting], name: str) -> Setting:
    """
    Retrieve a Setting from a list by its name.

    :param settings: List of Setting objects
    :param name: The name of the setting to find
    :return: The Setting object with the matching name
    :raises ValueError: If no setting with the given name is found
    """
    for setting in settings:
        if setting.name == name:
            return setting
    raise ValueError(f"Setting with name '{name}' not found.")


print('done processing settings')