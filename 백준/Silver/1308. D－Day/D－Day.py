import datetime

a_year, a_month, a_date = map(int, input().split())
b_year, b_month, b_date = map(int, input().split())

a = datetime.datetime(a_year, a_month, a_date)
b = datetime.datetime(b_year, b_month, b_date)

if (b-a).days >= 365243:
    print('gg')
else:
    print(f'D-{(b-a).days}')


