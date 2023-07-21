from collections import Counter


class Strategy:

    def __init__(self):
        self.opening_targets = [
            ("land", 3),
            ("ramp", 1),
            ("counter", 99),
            ("protection", 99),
            ("draw", 99),
            ("ability_doubler", 99),
            ("removal", 99),
            ("drannith magistrate", 99),
            ("tutorable_enchantment", 99),
        ]

    def get_opening_hand(self, cards, num_to_keep):
        # TODO: dar um refactor nisto, tá outra vez esparguete por causa do código fora do loop
        to_keep = []
        for type_tuple in self.opening_targets:
            kept = 0
            for card in cards:
                if kept < type_tuple[1] and card.role_tag == type_tuple[0]:
                    to_keep.append(card)
                    kept += 1
                    if len(to_keep) == num_to_keep:
                        to_put_back = [c for c in cards if c not in to_keep]
                        return to_keep, to_put_back

        # this means we couldn't complete a hand
        to_put_back = [c for c in cards if c not in to_keep]
        delta = num_to_keep - len(to_keep)
        to_keep = to_keep + to_put_back[:delta]
        to_put_back = [c for c in cards if c not in to_keep]
        return to_keep, to_put_back

    def mulligan_strat(self, hand, mull_counter):
        stats = self.__get_tag_stats(hand)

        if mull_counter < 5:
            if stats["land"] >= 3 and stats["ramp"] >= 1:
                return "Success"
        else:
            return "Fail"

    def run_turn_strat(self, hand, command_zone, max_mana):
        hand_deltas = []
        field_deltas = []
        grave_deltas = []
        command_zone_deltas = []

        max_mana_deltas = []

        current_mana = max_mana

        # 1-play land
        for c in list(hand):
            if c.role_tag == "land":
                hand_deltas.append((c, '-'))
                field_deltas.append((c, '+'))
                max_mana_deltas.append((1, '+'))
                hand.remove(c)
                break

        # 2-check for commander play
        if command_zone and command_zone[0].cmc <= current_mana:
            current_mana -= command_zone[0].cmc
            command_zone_deltas = [(command_zone[0], '-')]
            field_deltas = [(command_zone[0], '+')]

        # 3-play ramp
        for c in list(hand):
            if c.role_tag == "ramp" and c.cmc <= current_mana:
                current_mana -= c.cmc
                hand_deltas.append((c, '-'))
                field_deltas.append((c, '+'))
                max_mana_deltas.append((1, '+'))
                hand.remove(c)

        return hand_deltas, field_deltas, grave_deltas, command_zone_deltas, max_mana_deltas, current_mana

    def __get_tag_stats(self, hand):
        tags = []
        for card in hand:
            tags.append(card.role_tag)

        return Counter(tags)
