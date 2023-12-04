def sum_of_points(file_name):
    total = 0

    with open(file_name, "r") as file:
        text = file.read().splitlines()

    for line in text:
        card_score = 0
        cards = []
        colon_index = line.index(":")
        card = line[colon_index + 1 : :]
        guess, result = card.split("|")
        guess = guess.strip().split(" ")
        result = result.strip().split(" ")
        guess = [int(x.strip()) for x in guess if x.strip()]
        result = [int(x.strip()) for x in result if x.strip()]

        for g in guess:
            if g in result:
                cards.append(g)
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2
        print(card_score)
        total += card_score

    return total


# print(sum_of_points("day4/example.txt"))  # 13
print(sum_of_points("day4/puzzle.txt"))  # 1st 44681; final 22488
