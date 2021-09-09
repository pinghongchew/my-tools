import json
from os import dup
import random
traits_list = []
max_items = 10000

# import json config
with open('random_layers.json') as file:
    layers = json.load(file)
layers_count = len(layers)

# 1. check if all layers = 100%
# 2. assign traits to traits_list by percentage
# i = iteration of layers
for i in range(layers_count):
    traits_list.append([])
    traits = layers[f'layer_{ i + 1 }']
    total_percentage = 0
    # j = iteration of traits
    for j in range(len(traits)):
        trait_percentage = traits[f'trait_{ j + 1 }']
        # k = iteration to assign traits
        for k in range(trait_percentage):
            traits_list[i].append(j + 1)
        total_percentage += trait_percentage
    if total_percentage != 100:
        print(f'ERROR! Percentage (layer_{ i + 1 }) != 100')
        exit()

# read result file to memory
with open('layers_result.txt') as file:
    lines = file.readlines()

# shuffle array
for i in range(layers_count):
    random.shuffle(traits_list[i])

print(traits_list[0])
print(traits_list[1])
print(traits_list[2])
print(traits_list[3])
print(traits_list[4])
print(traits_list[5])
print(traits_list[6])

# iterate for items
for i in range(max_items):
    layers_result = ''
    duplicate = False
    # generate random number base on layers, eg: 7,7,9,4,3
    for j in range(layers_count):
        random_number = random.randint(0, 99)
        # random_number = round(random.uniform(0, 99))
        if j == layers_count - 1:
            layers_result += str(traits_list[j][random_number]) + '\n'
        else: 
            layers_result += str(traits_list[j][random_number]) + ','

    # check number if generated number duplicate
    for j in range(len(lines)):
        if lines[j] == layers_result:
            duplicate = True
            break
    
    # append to result if number is not duplicated
    if duplicate == False:
        lines.append(layers_result)

# write to result file
with open('layers_result.txt', 'w') as file:
    file.writelines(lines)

# print(traits_list)
# print(layers_result)

