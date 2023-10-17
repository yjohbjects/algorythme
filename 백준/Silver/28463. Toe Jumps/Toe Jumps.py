direction = {
    'W': {'P..O': 'T', '.IP.': 'F', '.OP.':'Lz'},
    'S': {'.OP.': 'T', 'I..P': 'F', 'O..P':'Lz'},
    'E': {'O..P': 'T', '.PI.': 'F', '.PO.':'Lz'},
    'N': {'.PO.': 'T', 'P..I': 'F', 'P..O':'Lz'}}

D = input()
a = input()
b = input()

if a+b in direction[D].keys():
    print(direction[D][a+b])
else:
    print('?')