import re

# 12 red, 13 green, 14 blue
bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open('input.txt', 'r') as file:
    data = file.read()

row = data.split('\n')

part_1_total = 0
part_2_total = 0

for game in row: 

    game_id_p = re.compile(r'Game (\d*)')
    green_p = re.compile(r'(\d*)\sgreen')
    red_p = re.compile(r'(\d*)\sred')
    blue_p = re.compile(r'(\d*)\sblue')

    green_list = re.findall(green_p, game)
    red_list = re.findall(red_p, game)
    blue_list = re.findall(blue_p, game)
    game_id = game_id_p.search(game).group(1)
    
    green_int_list = [int(i) for i in green_list]
    red_int_list = [int(i) for i in red_list]
    blue_int_list = [int(i) for i in blue_list]

    if (max(blue_int_list) <= bag["blue"] and max(red_int_list) <= bag['red'] and max(green_int_list) <= bag['green']):
        part_1_total += int(game_id)

    part_2_total += (max(green_int_list)*max(red_int_list)*max(blue_int_list))

print(part_1_total)
print(part_2_total)


