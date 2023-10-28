year=2015
is_leap= year%4==0 and year%100!=0 or year%400==0
print('The year', year, 'is leap:', is_leap)

