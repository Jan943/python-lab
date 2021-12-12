import os

def list_structure(dir, deep):
    directories = os.listdir(dir)
    for i in range(0, len(directories)):
        if(os.path.isdir(dir + f'/{directories[i]}')):
            print(f'{deep}{directories[i]}')
            newDir = dir + f'/{directories[i]}'
            newDeep = deep + f'./'
            list_structure(newDir, newDeep)
        else:
            print(f'{deep}{directories[i]}')

list_structure(os.getcwd(), '')