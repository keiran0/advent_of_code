with open('input.txt', 'r') as file:
    directions = file.read()

# Part 1

def get_house_coordinates(direction_string): #returns (x,y) of each house given a direction string
    up = direction_string.count('^')
    down = direction_string.count('v')
    left = direction_string.count('<')
    right = direction_string.count('>')
    return (left-right, up-down)

house_presents = {}

for i in range(len(directions) + 1):
    house_coordinates = get_house_coordinates(directions[:i])
    if house_presents.get(house_coordinates) is None:
        house_presents[house_coordinates] = 1
    else:
        house_presents[house_coordinates] += 1

print(len(house_presents))

# Part 2

santa_moves = directions[::2]
robo_santa_moves = directions[1::2]

house_presents = {}

print(get_house_coordinates(robo_santa_moves[:1]))

for i in range(len(santa_moves) + 1):
    house_coordinates = get_house_coordinates(santa_moves[:i])
    if house_presents.get(house_coordinates) is None:
        house_presents[house_coordinates] = 1
    else:
        house_presents[house_coordinates] += 1

for i in range(len(robo_santa_moves) + 1):
    house_coordinates = get_house_coordinates(robo_santa_moves[:i])
    if house_presents.get(house_coordinates) is None:
        house_presents[house_coordinates] = 1
    else:
        house_presents[house_coordinates] += 1

print(len(house_presents))