import json
import logging


def get_settings(filename: str) -> tuple:
    """Read json file with session settings and return them in separate valuables as either strings or dictionaries.

    Return content:

    settings: title (str), intro (str), card_shuffle (str)
    features:
        feature1: feature 1 settings (dict: name (str), value (int), visible (bool))
        feature2: feature 2 settings (dict: name (str), value (int), visible (bool))
        feature3: feature 3 settings (dict: name (str), value (int), visible (bool))
        feature4: feature 4 settings (dict: name (str), value (int), visible (bool))
    conditions: win/lose conditions (dict:
        win (dict: text (str), out_of_cards (bool), feature_values (list of int or None)
        lose (dict: text (str), out_of_cards (bool), feature_values (list of int or None)
        )
    cards: information about cards (list of dicts, each dict represents a card and contains:
        cta (str),
        left_action (dict: text (str), impact (list of ints)),
        right_action (dict: text (str), impact (list of ints))
    """
    with open(filename) as file:
        try:
            settings = json.load(file)
            # TODO Extensive check if json file is in correct format
            logging.debug(f"Successfully loaded settings from {filename}")
            features = settings.pop('features')
            conditions = settings.pop('conditions')
            cards = settings.pop('cards')
            return settings, features, conditions, cards

        except Exception as e:
            logging.exception("Exception occurred! Error message:")
            input("\nPlease ENTER to start over...")
