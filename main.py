from game import calculate_statistics, pets, select_pet
from storage import load_game, save_game


MENU_OPTIONS = [
    "Select a Tamagotchi",
    "Feed",
    "Play",
    "Sleep",
    "Heal",
    "Display Pet Status",
    "Game Statistics",
    "Save Game",
    "Load Game",
]

PET_ACTIONS = ("2", "3", "4", "5")
PET_OPTIONS = (*PET_ACTIONS, "6")

VALID_CHOICES = {
    str(index)
    for index in range(len(MENU_OPTIONS) + 1)
}


def display_menu():
    """Display the main game menu."""

    print("\n========== TAMAGOTCHI SIMULATOR ==========")

    for index, option in enumerate(MENU_OPTIONS, start=1):
        print(f"{index}. {option}")

    print("0. Quit")
    print("=========================================")


def display_statistics():
    """Calculate and display game statistics."""

    (
        living_count,
        dead_count,
        average_health,
        average_hunger,
        average_boredom,
        average_exhaustion,
    ) = calculate_statistics()

    print("\n========== GAME STATISTICS ==========")
    print(f"Living pets: {living_count}")
    print(f"Dead pets: {dead_count}")
    print(f"Average health: {average_health:.2f}")
    print(f"Average hunger: {average_hunger:.2f}")
    print(f"Average boredom: {average_boredom:.2f}")
    print(f"Average exhaustion: {average_exhaustion:.2f}")
    print("=====================================")


def perform_pet_action(pet, choice):
    """Perform the selected action and update the pet's condition."""

    if not pet.is_alive():
        print(f"{pet.name} is dead and cannot perform actions.")
        return

    if choice == "2":
        pet.feed()
        print(f"{pet.name} has been fed!")

    elif choice == "3":
        pet.play()
        print(f"{pet.name} has played!")

    elif choice == "4":
        pet.sleep()
        print(f"{pet.name} has slept!")

    elif choice == "5":
        pet.heal()
        print(f"{pet.name} has been healed!")

    pet.update_status()

    if pet.is_alive():
        pet.random_event()

    if not pet.is_alive():
        print(f"{pet.name} has died!")


def main():
    """Run the Tamagotchi simulator's interactive game loop."""

    selected_pet = None

    while True:
        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in VALID_CHOICES:
            print("Invalid choice. Please try again.")
            continue

        if choice == "1":
            pet = select_pet()

            if pet is not None:
                selected_pet = pet
                print(f"You selected {selected_pet.name}!")

        elif choice in PET_OPTIONS:
            if selected_pet is None:
                print("Please select a Tamagotchi first.")
                continue

            if choice == "6":
                selected_pet.display_status()

            else:
                perform_pet_action(selected_pet, choice)

        elif choice == "7":
            display_statistics()

        elif choice == "8":
            save_game(pets)

        elif choice == "9":
            loaded_pets = load_game()

            if loaded_pets is not None:
                pets[:] = loaded_pets
                selected_pet = None


if __name__ == "__main__":
    main()