from setting import S, BS

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



print('done processing settings')