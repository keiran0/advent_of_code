with open('input.txt', 'r') as file:
    presents = file.read().splitlines()

# Part 1

def required_wp(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l])

total_wp = 0

for dimensions in presents:
    measurements_string = dimensions.split('x')
    boxl, boxw, boxh = [int(measurement) for measurement in measurements_string]
    total_wp += required_wp(boxl, boxw, boxh)

print(total_wp)

# Part 2

def required_ribbon(l, w, h):
    return min([2*l+2*w, 2*w+2*h, 2*h+2*l]) + l*w*h

total_ribbon = 0

for dimensions in presents:
    measurements_string = dimensions.split('x')
    boxl, boxw, boxh = [int(measurement) for measurement in measurements_string]
    total_ribbon += required_ribbon(boxl, boxw, boxh)

print(total_ribbon)


