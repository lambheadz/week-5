from datetime import date, timedelta
tod = date.today()
yest = date.today() - timedelta(1)
tom = date.today() + timedelta(1)
print(yest)
print(tod)
print(tom)