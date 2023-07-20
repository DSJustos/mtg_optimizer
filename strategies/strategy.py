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
        # TODO: dar um refactor nisto, tá ganda esparguete com estes breaks todos
        to_keep = []
        while len(to_keep) < num_to_keep:
            for type_tuple in self.opening_targets:
                if len(to_keep) == num_to_keep:
                    break
                kept = 0
                for card in cards:
                    if kept < type_tuple[1] and card.role_tag == type_tuple[0]:
                        to_keep.append(card)
                        kept += 1
                        if len(to_keep) == num_to_keep:
                            break

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
