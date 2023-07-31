from itertools import combinations
word = input()

possibles = [i for i in range(len(word))]

test = list(combinations(possibles, 2))

temp = []
for t in test:
    first_stop = t[0]
    second_stop = t[1]

    a = word[first_stop::-1] 
    b = word[second_stop:first_stop:-1] 
    c = word[:second_stop:-1]
    if a and b and c:
        temp.append(a+b+c)

temp.sort()
print(temp[0])