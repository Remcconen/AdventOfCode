import numpy as np

def read_input(input):
    f = open(input, "r")
    bingo_numbers = np.fromstring(f.readline().rstrip(), dtype=int, sep=',')
    bingo_cards = []

    while True:
        line = f.readline()
        if not line:
            break

        card = np.zeros(shape=(5,5))
        for i in range (0, 5):
            card[i] = np.fromstring(f.readline().rstrip(), dtype=int, sep=' ')
        bingo_cards.append(card)

    return (bingo_numbers, bingo_cards)

def find_bingo(bingo_input, bingo_cards, bingo_card_results = []):
    if (len(bingo_card_results) == 0):
        for i in range(0, len(bingo_cards)):
            bingo_card_results.append(np.zeros(shape=(5,5), dtype=bool))

    for input in bingo_input:
        for i in range(0, len(bingo_cards)):
            input_found = np.where(bingo_cards[i] == input)
            if (input_found[0].size != 0):
                bingo_card_results[i][input_found[0], input_found[1]] = True

                # Check if BINGO
                if ((5 in np.sum(bingo_card_results[i], axis=0)) or (5 in np.sum(bingo_card_results[i], axis=1))):
                    return bingo_card_results, i, input

def bingo_sum(bingo_card, bingo_card_result, number):
    return np.sum(np.multiply(bingo_card, np.invert(bingo_card_result))) * number


def solve_1(bingo_input, bingo_cards):
    (bingo_card_results, index, input) = find_bingo(bingo_input, bingo_cards)

    bingo_card = bingo_cards[index]
    bingo_card_result = bingo_card_results[index]
    print("Bingo card:\n", bingo_card)
    print("Bingo card result:\n", bingo_card_result)
    print("Last number:", input)
    return bingo_sum(bingo_card, bingo_card_result, input)

def solve_2(bingo_input, bingo_cards):
    bingo_card_results = []
    while True:
        (bingo_card_results, index, input) = find_bingo(bingo_input, bingo_cards, bingo_card_results)
        if len(bingo_cards) == 1:
            break
        bingo_cards = np.delete(bingo_cards, index, axis=0)
        bingo_card_results = np.delete(bingo_card_results, index, axis=0)
        bingo_input = np.delete(bingo_input, np.arange(np.where(bingo_input == input)[0]), axis=0)
    
    bingo_card = bingo_cards[0]
    bingo_card_result = bingo_card_results[0]
    print("Bingo card:\n", bingo_card)
    print("Bingo card result:\n", bingo_card_result)
    print("Last number:", input)
    return bingo_sum(bingo_card, bingo_card_result, input)


(bingo_input, bingo_cards) = read_input("2021/4/input.txt")
print("Solution 1:", solve_1(bingo_input, bingo_cards))
print("Solution 2:", solve_2(bingo_input, bingo_cards))