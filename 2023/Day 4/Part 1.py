with open('input.txt','r') as file:
    data = file.read().split('\n')

total_points = 0

for row in data:
    points = 0
    card_number = row[5:8]
    winning_numbers = []
    numbers_i_have = []
    for i in range(10, 39, 3):
        winning_numbers.append(int(row[i] + row[i+1]))
    for i in range(42, 115, 3):
        numbers_i_have.append(int(row[i]+row[i+1]))
    
    for number in numbers_i_have:
        if number in winning_numbers:
            if points == 0:
                points += 1
            else:
                points *= 2
    total_points += points
    
print(total_points)
