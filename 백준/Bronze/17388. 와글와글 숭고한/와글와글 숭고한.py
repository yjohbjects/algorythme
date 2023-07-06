sungsil, korea, hanyang = map(int, input().split())

if (sungsil + korea + hanyang) >= 100:
    print('OK')
else:
    if min(sungsil, korea, hanyang) == sungsil:
        print('Soongsil')
    elif min(sungsil, korea, hanyang) == korea:
        print('Korea')
    else:
        print('Hanyang')