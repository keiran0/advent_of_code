import re

with open('input.txt', 'r') as file:
    calibration_data = file.read()

total = 0

for row in calibration_data.split('\n'):
    var = re.findall(r'\d', row)
    total += int(var[0] + var[-1])

print(total)