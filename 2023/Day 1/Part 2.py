import re

with open('input.txt', 'r') as file:
    calibration_data = file.read()

total = 0

def getRowCalibration(string):
    number_and_string_list = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', string)
    digits = number_and_string_list[0] + number_and_string_list[-1]
    x = ''
    x = digits.replace("one", "1") 
    x =  x.replace("two", "2")
    x =  x.replace("three", "3")
    x =  x.replace("four", "4")
    x =  x.replace("five", "5")
    x =  x.replace("six", "6")
    x =  x.replace("seven", "7")
    x =  x.replace("eight", "8")
    x =  x.replace("nine", "9")
    return(int(x))

for row in calibration_data.split('\n'):
    total += getRowCalibration(row)

print(total)
