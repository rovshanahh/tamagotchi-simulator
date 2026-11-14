from tamagotchi import Tamagotchi


# Initialize the game's three Tamagotchis
pets = [
    Tamagotchi("Kiwi"),
    Tamagotchi("Coco"),
    Tamagotchi("Pixel"),
]


def select_pet():
    """Display available Tamagotchis and return the selected pet."""

    print("\n========== SELECT A TAMAGOTCHI ==========")

    for index, pet in enumerate(pets, start=1):
        status = "Alive" if pet.is_alive() else "Dead"
        print(f"{index}. {pet.name} ({status})")

    print("0. Cancel")
    print("========================================")

    while True:
        try:
            choice = int(input("Enter your choice: ").strip())

            if choice == 0:
                return None

            if 1 <= choice <= len(pets):
                return pets[choice - 1]

            print("Invalid selection. Please choose an existing pet.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_statistics():
    """Calculate pet counts and average attributes of living pets."""

    living_count = 0
    dead_count = 0

    total_health = 0
    total_hunger = 0
    total_boredom = 0
    total_exhaustion = 0

    for pet in pets:
        if pet.is_alive():
            living_count += 1

            total_health += pet.health
            total_hunger += pet.hunger
            total_boredom += pet.boredom
            total_exhaustion += pet.exhaustion

        else:
            dead_count += 1

    if living_count > 0:
        average_health = total_health / living_count
        average_hunger = total_hunger / living_count
        average_boredom = total_boredom / living_count
        average_exhaustion = total_exhaustion / living_count

    else:
        average_health = 0
        average_hunger = 0
        average_boredom = 0
        average_exhaustion = 0

    return (
        living_count,
        dead_count,
        average_health,
        average_hunger,
        average_boredom,
        average_exhaustion,
    )