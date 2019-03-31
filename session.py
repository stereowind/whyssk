import os
import sys
from get_settings import get_settings
from classes import Settings, Feature, Condition, CardDeck, Card

# Session objects
settings = None
feature1 = None
feature2 = None
feature3 = None
feature4 = None
win = None
lose = None
deck = None
features_total = []


def clear() -> None:
    """Clears the screen"""
    _ = os.system("cls") if os.name == "nt" else os.system("clear")


def condition_check() -> str:
    """Checks if win or lost conditions are met this round"""
    global features_total, deck, win, lose
    # Reset value to min or max if out of bounds
    for feature in features_total:
        if feature.value < 0:
            feature.value = 0
        elif feature.value > 100:
            feature.value = 100

    # Check for lose conditions
    if lose.out_of_cards and len(deck.cards) == 0:
        return 'lose'
    for idx, feature in enumerate(features_total):
        if lose.feature_values[idx] is not None:
            if feature.value <= lose.feature_values[idx]:
                return 'lose'

    # Check for win conditions
    if win.out_of_cards and len(deck.cards) == 0:
        return 'win'
    for idx, feature in enumerate(features_total):
        if win.feature_values[idx] is not None:
            if feature.value >= win.feature_values[idx]:
                return 'win'


def status() -> None:
    """Prints current status"""
    clear()
    print("\n")
    global features_total
    for feature in features_total:
        if feature.visible:
            pipes = "|" * (int(feature.value) // 5)
            spaces = " " * (20 - len(pipes))
            print(f"{feature.name}: [{pipes}{spaces}]")
    print("\n")


# Initialize session and import data
def initialize() -> None:
    """Starts a new game session.
    Class objects used in the session:
    Settings:
        .title: Session title
        .intro: Session intro
        .card_shuffle: Shuffle cards or not
        .feature1: Feature 1 parameters
        .feature2: Feature 2 parameters
        .feature3: Feature 3 parameters
        .feature4: Feature 4 parameters
        .win: Win conditions
        .lose: Lose conditions
    CardDeck:
        .cards: Current number of cards in the deck
    Card:
        .cta: Current card's Call To Action
        .left_action: Left action parameters
        .right_action: Right action parameters
    """

    # Welcome screen
    clear()
    print("=" * 20)
    print("Welcome to Whyssk!")
    print("=" * 20 + "\n")

    # Ask for session settings file
    while True:
        filename = str(input("Please enter session settings file name (must be located inside sessions/ folder):\n"))
        if not filename.endswith(".json"):
            filename += ".json"
        path = str(os.path.realpath(sys.argv[0])) + "/sessions/" + filename
        print(path)
        if not os.path.exists(path):
            print(f"File {filename} does not exist in sessions/ folder!\n")
        else:
            print(f"File {filename} found! Importing...\n")
            break

    # Import settings from json file and create class instances
    sett, feat, cond, cards = get_settings(path)
    global settings, feature1, feature2, feature3, feature4, win, lose, deck, features_total
    settings = Settings(sett)
    feature1 = Feature(feat['feature1'])
    feature2 = Feature(feat['feature2'])
    feature3 = Feature(feat['feature3'])
    feature4 = Feature(feat['feature4'])
    win = Condition(cond['win'])
    lose = Condition(cond['lose'])
    deck = CardDeck(cards)

    if win.out_of_cards == lose.out_of_cards:
        raise ValueError("Win and lose conditions should have opposite values for 'out of cards' parameter!")

    # Generate list of features that will be used in game
    for feature in [feature1, feature2, feature3, feature4]:
        if feature.name:
            features_total.append(feature)

    print("Import successful!")
    input("Press ENTER to start the session!")
    clear()


def main() -> None:
    """Main session flow"""
    global settings, feature1, feature2, feature3, feature4, win, lose, deck, features_total
    result = None
    print("\n" + settings.intro)
    input("\n\n\nPress ENTER to start!")
    while len(deck.cards) > 0:
        card = Card(deck)
        # Check if win or lose conditions are met
        result = condition_check()
        if result == "lose" or result == "win":
            break
        # Loop below re-executes if input was different from "l" or "r"
        while True:
            status()  # Prints current status screen
            print(card.cta + "\n")
            print(f"Left: {card.l_text}")
            print(f"Right: {card.r_text}")
            choice = input("\nChoose your destiny! [l/r]:\n")
            if choice.lower() == 'l':
                for idx, feature in enumerate(features_total):
                    feature.value += card.l_impact[idx]
                break
            elif choice.lower() == 'r':
                for idx, feature in enumerate(features_total):
                    feature.value += card.r_impact[idx]
                break
        clear()

    # End of session
    if result == 'win':
        print("\nYOU WON!\n")
        print(win.text)
    elif result == 'lose':
        print("\nYOU LOST!\n")
        print(lose.text)
    input("\n\nPress ENTER to exit...")

    # Clean up
    for _ in [settings, feature1, feature2, feature3, feature4, win, lose, deck]:
        _ = None
    features_total = []
    clear()
