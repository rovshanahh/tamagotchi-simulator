import json

from tamagotchi import Tamagotchi


SAVE_FILE = "savegame.json"

REQUIRED_ATTRIBUTES = (
    "hunger",
    "health",
    "boredom",
    "exhaustion",
)

MIN_STATUS = 0
MAX_STATUS = 100


def validate_pet_data(pet_data):
    """Validate a pet's saved attributes before reconstruction."""

    if not isinstance(pet_data, dict):
        return False

    name = pet_data.get("name")

    if not isinstance(name, str) or not name.strip():
        return False

    for attribute in REQUIRED_ATTRIBUTES:
        value = pet_data.get(attribute)

        if type(value) is not int:
            return False

        if not MIN_STATUS <= value <= MAX_STATUS:
            return False

    return True


def save_game(pets):
    """Save all Tamagotchi attributes to a JSON file."""

    pets_data = []

    for pet in pets:
        pet_data = {
            "name": pet.name,
            "hunger": pet.hunger,
            "health": pet.health,
            "boredom": pet.boredom,
            "exhaustion": pet.exhaustion,
        }

        pets_data.append(pet_data)

    game_data = {"pets": pets_data}

    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(game_data, file, indent=4)

    except OSError as error:
        print(f"Error saving game: {error}")
        return False

    print("Game saved successfully!")
    return True


def load_game():
    """Load and reconstruct Tamagotchi objects from a JSON file."""

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            game_data = json.load(file)

        if not isinstance(game_data, dict):
            raise ValueError("Invalid save file structure.")

        pets_data = game_data.get("pets")

        if not isinstance(pets_data, list):
            raise ValueError("Invalid pets list in save file.")

        if len(pets_data) != 3:
            raise ValueError("The save file must contain exactly three pets.")

        loaded_pets = []

        for pet_data in pets_data:
            if not validate_pet_data(pet_data):
                raise ValueError("Invalid pet data in save file.")

            pet = Tamagotchi(pet_data["name"])

            pet.hunger = pet_data["hunger"]
            pet.health = pet_data["health"]
            pet.boredom = pet_data["boredom"]
            pet.exhaustion = pet_data["exhaustion"]

            loaded_pets.append(pet)

    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Error loading game: {error}")
        return None

    print("Game loaded successfully!")
    return loaded_pets