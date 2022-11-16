import yaml
import os

#declare path
path = (r"C:\Users\conno\Downloads\sethomes - Copy")
os.chdir(path)

#main function
def readfile(file_path):   
    with open(file_path, "r", encoding='utf-8', errors='ignore') as f:
        #read file and get first essential data
        data = yaml.load(f, Loader=yaml.SafeLoader)
        print(data)
        name = data.get('name')
        homes = data.get('homes')
        #serach through all the homes of the user and their coords/world
        with open('file_data.txt', 'a', encoding='utf-8') as file:
            file.write('\n'+ name + ':' + '\n')
            if homes != None:
                for key in homes:
                    coords = homes[key].get('coords')
                    world = homes[key].get('world-name')
                    file.write(key + ', ' + coords + ', ' + world + '\n')
            else:
                pass

#go through all the different files          
for file in os.listdir():
    if file.endswith(".yml"):
        file_path = f"{path}\{file}"
        readfile(file_path)