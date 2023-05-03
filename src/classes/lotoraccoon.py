import random


class LotoRaccoon:
    def __init__(self, lottery_history):
        self.lottery_history = lottery_history

    def get_lotto_sequence(self):
        sequence = []
        sequence.append(random.choice([x[0] for x in self.lottery_history]))
        sequence.append(random.choice([x[1] for x in self.lottery_history]))
        sequence.append(random.choice([x[2] for x in self.lottery_history]))
        sequence.append(random.choice([x[3] for x in self.lottery_history]))
        sequence.append(random.choice([x[4] for x in self.lottery_history]))
        sequence.append(random.choice([x[5] for x in self.lottery_history]))
        return sequence
