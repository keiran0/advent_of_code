with open('input.txt','r') as file:
    data = file.read().split('\n')

cards = []

for row in data:
    
    card_number = int(row[5:8])
    winning_numbers = []
    numbers_i_have = []
    matches = 0

    for i in range(10, 39, 3):
        winning_numbers.append(int(row[i] + row[i+1]))
    for i in range(42, 115, 3):
        numbers_i_have.append(int(row[i]+row[i+1]))

    points = 0
    for number in numbers_i_have:
        if number in winning_numbers:
            matches += 1
            if points == 0:
                points += 1
            else:
                points *= 2
    
    details = {
        "card_number": card_number,
        "matches": matches,
        "quantity": 1
    }
    cards.append(details)

for i in range(len(cards)):
    if cards[i]["quantity"] > 0:
        for m in range(cards[i]["matches"]):
            cards[m+1+i]["quantity"] += cards[i]["quantity"]

print(sum(card["quantity"] for card in cards))



