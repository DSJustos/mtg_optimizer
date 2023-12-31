from mtg_optimizer.structs.card_structs import Card, Deck


def BACKUP_build_zur():
    # https://www.moxfield.com/decks/0Sen3s0QckGmWvp4XlIyiA
    zur = Card(role_tag="commander")

    decklist = []

    for i in range(33):
        decklist.append(Card(role_tag="land"))

    for i in range(10):
        decklist.append(Card(role_tag="ramp"))

    for i in range(26):
        decklist.append(Card(role_tag="tutorable_enchantment"))

    for i in range(2):
        decklist.append(Card(role_tag="protection"))

    for i in range(2):
        decklist.append(Card(role_tag="ability_doubler"))

    for i in range(1):
        decklist.append(Card(role_tag="drannith magistrate"))

    for i in range(2):
        decklist.append(Card(role_tag="draw"))

    for i in range(9):
        decklist.append(Card(role_tag="removal"))

    for i in range(14):
        decklist.append(Card(role_tag="counter"))

    return Deck(commander=zur, cards=decklist)


def build_zur():
    zur = Card(role_tag="commander", cmc=4)

    decklist = []

    for i in range(36):
        decklist.append(Card(role_tag="land", has_summoning_sickness=False))

    for i in range(11):
        decklist.append(Card(role_tag="ramp", cmc=2, has_summoning_sickness=False))

    decklist.append(Card(role_tag="ramp", cmc=1, has_summoning_sickness=False)) #sol ring

    for i in range(21):
        decklist.append(Card(role_tag="tutorable_enchantment"))

    for i in range(2):
        decklist.append(Card(role_tag="protection"))

    for i in range(2):
        decklist.append(Card(role_tag="ability_doubler", has_summoning_sickness=False))

    for i in range(1):
        decklist.append(Card(role_tag="drannith magistrate"))

    for i in range(2):
        decklist.append(Card(role_tag="draw"))

    for i in range(9):
        decklist.append(Card(role_tag="removal"))

    for i in range(10):
        decklist.append(Card(role_tag="counter", cmc=2))

    for i in range(3):
        decklist.append(Card(role_tag="counter", cmc=1))

    for i in range(1):
        decklist.append(Card(role_tag="counter", cmc=0))

    return Deck(commander=zur, cards=decklist)