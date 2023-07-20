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

    def __get_tag_stats(self, hand):
        tags = []
        for card in hand:
            tags.append(card.role_tag)

        return Counter(tags)
