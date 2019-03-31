class Settings:
    """General settings: title, intro, card_shuffle"""
    def __init__(self, settings):
        self.title = settings['title']
        self.intro = settings['intro']
        self.card_shuffle = settings['card_shuffle']


class Feature:
    """Represents each feature: name, value, visible"""
    def __init__(self, feature):
        self.name = feature['name']
        self.value = feature['value']
        self.visible = feature['visible']


class Condition:
    """Represents win or lose condition: text, out_of_cards, feature_values"""
    def __init__(self, condition):
        self.text = condition['text']
        self.out_of_cards = condition['out_of_cards']
        self.feature_values = condition['feature_values']


class CardDeck:
    """Represents whole deck of cards for the session: cards"""
    def __init__(self, cards):
        self.cards = cards


class Card:
    """Represents each card, gets popped from deck: cta, l_text, l_impact, r_text, r_impact"""
    def __init__(self, deck):
        self.card = deck.cards.pop(0)
        self.cta = self.card['cta']
        self.l_text = self.card['left_action']['text']
        self.l_impact = self.card['left_action']['impact']
        self.r_text = self.card['right_action']['text']
        self.r_impact = self.card['right_action']['impact']
