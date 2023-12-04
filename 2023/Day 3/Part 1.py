import re,json

pattern = re.compile(r'[\D|\s]*(\d*)[\D|\s]*')

with open('input.txt', 'r') as file:
    schematic = file.read()

def isSymbol(inp):
    if (inp.isnumeric() or inp == '.'):
        return False
    else:
        return True
    
data = []

for row in schematic.split('\n'): 

    ls = re.findall(pattern, row)

    row_details = {
        # "raw": row,
        "all_numbers": ls[0: len(ls)-1],
        "number_details": []
    }

    first_number_indexes = []
    for i in range(len(row_details["all_numbers"])):
        first_number_indexes.append(row.find(ls[i]))

    all_number_indexes = []

    for num in first_number_indexes:
        number_details = {
            "number": row_details["all_numbers"][first_number_indexes.index(num)],
            "indexes": []
        }
        all_number_indexes.append(num)
        number_details["indexes"].append(num)

        for y in range(len(number_details["number"])-1):
            all_number_indexes.append(y + num + 1)
            number_details["indexes"].append(y+num+1)
            
        row_details["number_details"].append(number_details)

    data.append(row_details)

schematic_list = []
for row in schematic.split('\n'):
    schematic_list.append(row)

list_of_indexes = []

for i in range(len(data)): 
    newls = []
    for y in data[i]["number_details"]:
        newls.extend(y["indexes"])
    list_of_indexes.append(newls)

for y in range(len(schematic_list)):
    #print(schematic_list[y])
    for x in range(len(schematic_list[y])):

        if y == len(schematic_list)-1 and x==len(schematic_list[y])-1:
            has_adjacent_symbol = isSymbol(schematic_list[x-1][y-1]) or isSymbol(schematic_list[x-1][y]) or isSymbol(schematic_list[x][y-1])

        elif y == 0 and x == 0:
            has_adjacent_symbol = isSymbol(schematic_list[y][x+1]) or isSymbol(schematic_list[y+1][x]) or isSymbol(schematic_list[y+1][x+1])

        elif y == 0 and x==len(schematic_list[y])-1:
            has_adjacent_symbol = isSymbol(schematic_list[x-1][y]) or isSymbol(schematic_list[x-1][y+1]) or isSymbol(schematic_list[x][y+1])

        elif y == len(schematic_list)-1 and x==0:
            has_adjacent_symbol = isSymbol(schematic_list[x][y-1]) or isSymbol(schematic_list[x+1][y-1]) or isSymbol(schematic_list[x+1][y])

        elif x == 0:
            has_adjacent_symbol = isSymbol(schematic_list[x][y-1]) or isSymbol(schematic_list[x][y+1]) or isSymbol(schematic_list[x+1][y-1]) or isSymbol(schematic_list[x+1][y]) or isSymbol(schematic_list[x+1][y+1])

        elif y == 0:
            has_adjacent_symbol = isSymbol(schematic_list[x-1][y]) or isSymbol(schematic_list[x-1][y+1]) or isSymbol(schematic_list[x][y+1]) or isSymbol(schematic_list[x+1][y]) or isSymbol(schematic_list[x+1][y+1])

        else:
            has_adjacent_symbol = isSymbol(schematic_list[x-1][y-1]) or isSymbol(schematic_list[x-1][y]) or isSymbol(schematic_list[x][y-1])

with open('output.json', 'w') as file:
    json.dump(data, file)
