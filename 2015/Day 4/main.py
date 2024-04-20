from hashlib import md5

with open('input.txt', 'r') as file:
    secret_key = file.read()

# Part 1

i = 0

while True:
    hash = md5(f'bgvyzdsv{i}'.encode()).hexdigest()
    if hash[0:5] == '00000':
        print(i)
        break
    i+=1

# Part 2

i = 0

while True:
    hash = md5(f'bgvyzdsv{i}'.encode()).hexdigest()
    if hash[0:6] == '000000':
        print(i)
        break
    i+=1
