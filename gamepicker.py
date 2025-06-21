


import random
from setting import Setting, BooleanSetting
def choose_item_with_seed(my_list, seed_value):
    """
Chooses an item from a list at random using a seed value.

Args:
my_list: The list to choose an item from.
seed_value: The seed value for the random number generator.

Returns:
The randomly chosen item from the list.
    """
    random.seed(seed_value)
    return random.choice(my_list)

# Define a sample list of items
my_favorite_fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Choose an item with a specific seed value
seed_key = 42
chosen_fruit_run1 = choose_item_with_seed(my_favorite_fruits, seed_key)
# print(f"Chosen fruit with seed {seed_key}: {chosen_fruit_run1}")

# Running it again with the same seed will produce the same result
chosen_fruit_run2 = choose_item_with_seed(my_favorite_fruits, seed_key)
# print(f"Chosen fruit with seed {seed_key} again: {chosen_fruit_run2}")

# Using a different seed will likely produce a different result
new_seed_key = 101
chosen_fruit_run3 = choose_item_with_seed(my_favorite_fruits, new_seed_key)
# print(f"Chosen fruit with seed {new_seed_key}: {chosen_fruit_run3}")

aoe2_game_modes = {"Random Map", "Empire Wars", "Death Match", "Regicide", "King of the Hill",
                          "Capture the Relic", "Wonder Race", "Defend the Wonder", "Sudden Death", "Battle Royale",
                          "Co-Op Campaign", "Custom Scenario"}

print(f"{aoe2_game_modes=}")

