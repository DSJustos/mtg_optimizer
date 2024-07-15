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


def build_zur(counts=[36, 11, 1, 21, 2, 2, 1, 2, 9, 10, 3, 1]):
    zur = Card(role_tag="commander", cmc=4)

    decklist = []

    for i in range(counts[0]):
        decklist.append(Card(role_tag="land", has_summoning_sickness=False))

    for i in range(counts[1]):
        decklist.append(Card(role_tag="ramp", cmc=2, has_summoning_sickness=False))

    for i in range(counts[2]):
        decklist.append(Card(role_tag="ramp", cmc=1, has_summoning_sickness=False))  # sol ring

    for i in range(counts[3]):
        decklist.append(Card(role_tag="tutorable_enchantment"))

    for i in range(counts[4]):
        decklist.append(Card(role_tag="protection"))

    for i in range(counts[5]):
        decklist.append(Card(role_tag="ability_doubler", has_summoning_sickness=False))

    for i in range(counts[6]):
        decklist.append(Card(role_tag="drannith magistrate"))

    for i in range(counts[7]):
        decklist.append(Card(role_tag="draw"))

    for i in range(counts[8]):
        decklist.append(Card(role_tag="removal"))

    for i in range(counts[9]):
        decklist.append(Card(role_tag="counter", cmc=2))

    for i in range(counts[10]):
        decklist.append(Card(role_tag="counter", cmc=1))

    for i in range(counts[11]):
        decklist.append(Card(role_tag="counter", cmc=0))

    return Deck(commander=zur, cards=decklist)

def build_winota(counts=[41, 5, 1, 8, 9, 5, 20, 5, 5]):
    # https://www.moxfield.com/decks/f4Ycc2x8FkCtX106nojhvw
    winota = Card(role_tag="commander", cmc=4)

    decklist = []

    for i in range(counts[0]):
        decklist.append(Card(role_tag="land", has_summoning_sickness=False))

    for i in range(counts[1]):
        decklist.append(Card(role_tag="ramp", cmc=2, has_summoning_sickness=False))

    for i in range(counts[2]):
        decklist.append(Card(role_tag="ramp", cmc=1, has_summoning_sickness=False))  # sol ring

    for i in range(counts[3]):
        decklist.append(Card(role_tag="ramp", cmc=2, has_summoning_sickness=True))

    for i in range(counts[3]):
        decklist.append(Card(role_tag="first_attacker", cmc=1, has_summoning_sickness=True))

    for i in range(counts[4]):
        decklist.append(Card(role_tag="first_attacker", cmc=0, has_summoning_sickness=True))

    for i in range(counts[5]):
        decklist.append(Card(role_tag="human", cmc=6, has_summoning_sickness=True))

    for i in range(counts[6]):
        decklist.append(Card(role_tag="haster", cmc=4, has_summoning_sickness=False))

    for i in range(counts[7]):
        decklist.append(Card(role_tag="haster", cmc=5, has_summoning_sickness=False))

    return Deck(commander=winota, cards=decklist)