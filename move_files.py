import os
from shutil import copyfile

with open('layers_result.txt') as file:
    lines = file.readlines()

# get next combination
line = ''
index = 0
for i in range(len(lines)):
    line = lines[i].split(',')
    index = i
    if line[0] != 'Done':
        break

# check all layers' folder exist
folders = os.listdir('traits')
for i in range(len(line)):
    if not 'layer' + str(i + 1) in folders:
        print(f'ERROR! Folder layer{i + 1} not existed')
        exit()

# copy files
for i in range(len(line)):
    layer = i + 1
    name = line[i].strip('\n')
    copyfile(f'traits/layer{layer}/{name}.txt', f'combine/layer{layer}.txt')

# mark as done
lines[index] = 'Done,' + lines[index]
with open('layers_result.txt', 'w') as file:
    file.writelines(lines)
