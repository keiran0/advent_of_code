with open('input.txt','r') as file:
    data = file.read().split('\n')

seeds = [int(seed) for seed in data[0][7:].split(' ')]
seed_to_soil_index = data.index('seed-to-soil map:')
soil_to_fertilizer_index = data.index('soil-to-fertilizer map:')
fertilizer_to_water_index = data.index('fertilizer-to-water map:')
water_to_light_index = data.index('water-to-light map:')
light_to_temperature_index = data.index('light-to-temperature map:')
temperature_to_humidity_index = data.index('temperature-to-humidity map:')
humidity_to_location_index = data.index('humidity-to-location map:')

seed_to_soil_map = data[seed_to_soil_index+1:soil_to_fertilizer_index-1]
soil_to_fertilizer_map = data[soil_to_fertilizer_index+1: fertilizer_to_water_index-1]
fertilizer_to_water_map = data[fertilizer_to_water_index+1:water_to_light_index-1]
water_to_light_map = data[water_to_light_index+1:light_to_temperature_index-1]
light_to_temperature_map = data[light_to_temperature_index+1:temperature_to_humidity_index-1]
temperature_to_humidity_map = data[temperature_to_humidity_index+1:humidity_to_location_index-1]
humidity_to_location_map = data[humidity_to_location_index+1:]

maps = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]

# destination range start, source range start, range length
def getDestination(source_number, map):
    for row in map:
        map_list = [int(data_str) for data_str in row.split(' ')]
        if source_number >= map_list[1] and source_number < map_list[1] + map_list[2]:
            difference = source_number - map_list[1]
            return difference + map_list[0]
    return source_number

results = []

for seed in seeds:
    result = ''
    result = getDestination(seed, seed_to_soil_map)
    for map in maps[1:]:
        result = getDestination(result, map)
    results.append(result)

print(min(results))