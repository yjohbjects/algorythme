mod = []
for i in range(1, 11):
    num = int(input())

    if num%42 not in mod:
        mod.append(num%42)

print(len(mod))
