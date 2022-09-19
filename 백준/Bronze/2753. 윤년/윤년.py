year = int(input())

# 윤년
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(1)
# 안윤년
else:
    print(0)