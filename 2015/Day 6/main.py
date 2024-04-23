import re

with open('input.txt','r') as file:
    instructions = file.read().splitlines()

# Part 1

lights = {}

for x in range(1000):
    for y in range(1000):
        lights[(x,y)] = 'off'

for instruction in instructions:
    op = re.findall(r'(off|on|toggle) (\d*),(\d*) through (\d*),(\d*)', instruction)[0]
    for x in range(int(op[1]),int(op[3])+1):
        for y in range(int(op[2]), int(op[4])+1):
            if op[0] == 'toggle':
                if lights[(x,y)] == 'on':
                    lights[(x,y)] = 'off'
                else:
                    lights[(x,y)] = 'on'
            else:
                lights[(x,y)] = op[0]

list_lights = list(lights.values())

print(list_lights.count('on'))

# Part 2

lights = {}

total_brightness = 0

for x in range(1000):
    for y in range(1000):
        lights[(x,y)] = 0

for instruction in instructions:
    op = re.findall(r'(off|on|toggle) (\d*),(\d*) through (\d*),(\d*)', instruction)[0]
    for x in range(int(op[1]),int(op[3])+1):
        for y in range(int(op[2]), int(op[4])+1):
            if op[0] == 'toggle':
                lights[(x,y)] += 2
            elif op[0] == 'off':
                if lights[(x,y)] != 0:
                    lights[(x,y)] -= 1
                pass
            else:
                lights[(x,y)] += 1

list_lights = list(lights.values())

for num in list_lights:
    total_brightness += num

print(total_brightness)