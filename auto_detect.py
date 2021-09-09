import os
from shutil import move
import time
from datetime import datetime

source = 'output'
dest = 'final'


while (True):
    dir = os.listdir('output')
    print('Files: ' + str(len(dir)))
    if len(dir) > 0:
        for i in range(len(dir)):
            datenow = datetime.now().strftime('%Y%m%d%H%M%S')
            move(f'{source}/{dir[i]}', f'{dest}/{datenow}_{dir[i]}')
            print('Move: ' + f'{source}/{dir[i]}' + ' to ' + f'{dest}/{datenow}_{dir[i]}')
            os.system('python move_files.py')
    
    time.sleep(0.5)

