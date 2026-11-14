import random


# Initial status values
INITIAL_HUNGER = 50
INITIAL_HEALTH = 100
INITIAL_BOREDOM = 50
INITIAL_EXHAUSTION = 0

# Status limits
MIN_STATUS = 0
MAX_STATUS = 100

# Action effects
FEED_REDUCTION = 20
PLAY_BOREDOM_REDUCTION = 20
PLAY_HUNGER_INCREASE = 10
PLAY_EXHAUSTION_INCREASE = 15
SLEEP_RECOVERY = 30
HEAL_RECOVERY = 25

# Natural status changes
HUNGER_INCREASE = 5
BOREDOM_INCREASE = 5
EXHAUSTION_INCREASE = 5

# Health penalties
STARVATION_DAMAGE = 10

# Random event effects
RANDOM_FOOD_REDUCTION = 10
RANDOM_SICKNESS_DAMAGE = 15
RANDOM_TOY_REDUCTION = 10

# Probability of triggering a random event
RANDOM_EVENT_PROBABILITY = 0.30

RANDOM_EVENTS = ("food", "sickness", "toy")


class Tamagotchi:
    """Represent a virtual pet with changing status attributes."""

    def __init__(self, name):
        """Initialize a Tamagotchi with its starting attributes."""
        self.name = name
        self.hunger = INITIAL_HUNGER
        self.health = INITIAL_HEALTH
        self.boredom = INITIAL_BOREDOM
        self.exhaustion = INITIAL_EXHAUSTION

    def is_alive(self):
        """Return True if the Tamagotchi is alive."""
        return self.health > MIN_STATUS

    def feed(self):
        """Reduce the pet's hunger."""
        if not self.is_alive():
            return

        self.hunger = max(
            self.hunger - FEED_REDUCTION,
            MIN_STATUS,
        )

    def play(self):
        """Reduce boredom while increasing hunger and exhaustion."""
        if not self.is_alive():
            return

        self.boredom = max(
            self.boredom - PLAY_BOREDOM_REDUCTION,
            MIN_STATUS,
        )

        self.hunger = min(
            self.hunger + PLAY_HUNGER_INCREASE,
            MAX_STATUS,
        )

        self.exhaustion = min(
            self.exhaustion + PLAY_EXHAUSTION_INCREASE,
            MAX_STATUS,
        )

    def sleep(self):
        """Reduce the pet's exhaustion."""
        if not self.is_alive():
            return

        self.exhaustion = max(
            self.exhaustion - SLEEP_RECOVERY,
            MIN_STATUS,
        )

    def heal(self):
        """Restore the pet's health."""
        if not self.is_alive():
            return

        self.health = min(
            self.health + HEAL_RECOVERY,
            MAX_STATUS,
        )

    def display_status(self):
        """Display the pet's current attributes and life status."""
        print(f"\n========== {self.name.upper()} ==========")
        print(f"Status: {'Alive' if self.is_alive() else 'Dead'}")
        print(f"Hunger: {self.hunger}")
        print(f"Health: {self.health}")
        print(f"Boredom: {self.boredom}")
        print(f"Exhaustion: {self.exhaustion}")
        print("=" * (22 + len(self.name)))

    def update_status(self):
        """Update the pet's condition as the game progresses."""
        if not self.is_alive():
            return

        self.hunger = min(
            self.hunger + HUNGER_INCREASE,
            MAX_STATUS,
        )

        self.boredom = min(
            self.boredom + BOREDOM_INCREASE,
            MAX_STATUS,
        )

        self.exhaustion = min(
            self.exhaustion + EXHAUSTION_INCREASE,
            MAX_STATUS,
        )

        if self.hunger >= MAX_STATUS:
            self.health = max(
                self.health - STARVATION_DAMAGE,
                MIN_STATUS,
            )

    def random_event(self):
        """Occasionally trigger an event that affects the pet."""
        if not self.is_alive():
            return

        if random.random() >= RANDOM_EVENT_PROBABILITY:
            return

        event = random.choice(RANDOM_EVENTS)

        if event == "food":
            self.hunger = max(
                self.hunger - RANDOM_FOOD_REDUCTION,
                MIN_STATUS,
            )
            print(f"{self.name} found some food! Hunger decreased.")

        elif event == "sickness":
            self.health = max(
                self.health - RANDOM_SICKNESS_DAMAGE,
                MIN_STATUS,
            )
            print(f"{self.name} got sick! Health decreased.")

        elif event == "toy":
            self.boredom = max(
                self.boredom - RANDOM_TOY_REDUCTION,
                MIN_STATUS,
            )
            print(f"{self.name} found a toy! Boredom decreased.")