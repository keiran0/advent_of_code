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
schematic_list = []

for row in schematic.split('\n'): 
    schematic_list.append(row)
    ls = re.findall(pattern, row)

    row_details = {
        "all_numbers": ls[0: len(ls)-1],
        "all_indexes": [],
        "number_details": []
    }

    first_number_indexes = []
    for i in range(len(row_details["all_numbers"])):
        first_number_indexes.append(row.find(ls[i]))


    for num in first_number_indexes:
        number_details = {
            "number": row_details["all_numbers"][first_number_indexes.index(num)],
            "indexes": []
        }
        number_details["indexes"].append(num)
        for y in range(len(number_details["number"])-1):
            number_details["indexes"].append(y+num+1)
            
        row_details["number_details"].append(number_details)

    data.append(row_details)

for i in range(len(data)): 
    for y in data[i]["number_details"]:
        data[i]["all_indexes"].extend(y["indexes"])

def hasAdjacentSymbol(y, x):
    try:
        if y == len(schematic_list)-1 and x==len(schematic_list[y])-1:
            return isSymbol(schematic_list[x-1][y-1]) or isSymbol(schematic_list[x-1][y]) or isSymbol(schematic_list[x][y-1])
        elif y == 0 and x == 0:
            return isSymbol(schematic_list[y][x+1]) or isSymbol(schematic_list[y+1][x]) or isSymbol(schematic_list[y+1][x+1])
        elif y == 0 and x==len(schematic_list[y])-1:
            return isSymbol(schematic_list[x-1][y]) or isSymbol(schematic_list[x-1][y+1]) or isSymbol(schematic_list[x][y+1])
        elif y == len(schematic_list)-1 and x==0:
            return isSymbol(schematic_list[x][y-1]) or isSymbol(schematic_list[x+1][y-1]) or isSymbol(schematic_list[x+1][y])
        elif x == 0:
            return isSymbol(schematic_list[x][y-1]) or isSymbol(schematic_list[x][y+1]) or isSymbol(schematic_list[x+1][y-1]) or isSymbol(schematic_list[x+1][y]) or isSymbol(schematic_list[x+1][y+1])
        elif y == 0:
            return isSymbol(schematic_list[x-1][y]) or isSymbol(schematic_list[x-1][y+1]) or isSymbol(schematic_list[x][y+1]) or isSymbol(schematic_list[x+1][y]) or isSymbol(schematic_list[x+1][y+1])
        elif x==len(schematic_list[y])-1:
            return isSymbol(schematic_list[x-1][y-1]) or isSymbol(schematic_list[x][y-1]) or isSymbol(schematic_list[x-1][y]) or isSymbol(schematic_list[x-1][y+1]) or isSymbol(schematic_list[x][y+1])
        elif y == len(schematic_list)-1:
            return isSymbol(schematic_list[x-1][y-1]) or isSymbol(schematic_list[x][y-1]) or isSymbol(schematic_list[x+1][y-1]) or isSymbol(schematic_list[x-1][y]) or isSymbol(schematic_list[x+1][y]) or isSymbol(schematic_list[x+1][y]) 
        else:
            return isSymbol(schematic_list[x-1][y-1]) or isSymbol(schematic_list[x][y-1]) or isSymbol(schematic_list[x+1][y-1]) or isSymbol(schematic_list[x-1][y]) or isSymbol(schematic_list[x+1][y]) or isSymbol(schematic_list[x+1][y]) or isSymbol(schematic_list[x-1][y+1]) or isSymbol(schematic_list[x][y+1]) or isSymbol(schematic_list[x+1][y+1]) 
    except IndexError:
        print(f'x{x} , y{y}')

towrite2 = ''
sum = 0

for y in range(len(data)):
    added = []
    towrite2 += f'\nThis is row {y}\n'
    for x in data[y]["all_indexes"]:
        if hasAdjacentSymbol(x, y): 
            towrite2 += f'Column {x} has a symbol adjacent to it.\n'
            for i in range(len(data[y]["number_details"])):
                if x in data[y]["number_details"][i]["indexes"]: 
                    num_to_add = int(data[y]["number_details"][i]["number"])
                    towrite2 += str(num_to_add)
                    towrite2 += '\n'
                    if num_to_add not in added:
                        
                        sum += num_to_add
                        added.append(num_to_add)
                    else:
                        towrite2 += 'This number has already been added. Skipping \n'
print(sum)


with open('output.txt','w') as file2:
    file2.write(towrite2)

with open('output.json', 'w') as file:
    json.dump(data, file)


