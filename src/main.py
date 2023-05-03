from classes.lotoraccoon import LotoRaccoon
from pprint import pprint


def main():
    history_file = open("HISTORY.txt", "r")
    history_content = history_file.read()
    data__raw_sequences, treated_sequences = history_content.split("\n"), []
    for sequence in data__raw_sequences:
        treated_sequences.append(sequence.split(" "))
    raccoon = LotoRaccoon(treated_sequences)
    pprint(raccoon.get_lotto_sequence())


if __name__ == "__main__":
    main()
