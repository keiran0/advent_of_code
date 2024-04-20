# Part 1

with open('input.txt', 'r') as file:
    original_instructions = file.read()

number_of_bracket_pairs = 0

instructions = original_instructions

while True:
    start_length = len(instructions)
    instructions = instructions.replace("()", "")
    
    if start_length == len(instructions):
        break
    else:
        number_of_bracket_pairs += 1

print(instructions.count("(") - instructions.count(")"))

# Part 2

instructions = original_instructions

floor = 0

for i in range(len(instructions)):

    if floor == -1:
        print(i)
        break

    if instructions[i] == '(':
        floor += 1
    else:
        floor -= 1