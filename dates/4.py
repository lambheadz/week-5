from datetime import datetime, time
def date_diff_sec(d2, d1):
    timedelta = d2 - d1
    return timedelta.days * 24 * 3600 + timedelta.seconds
d1 = datetime.strptime('2019-09-08 19:10:00', '%Y-%m-%d %H:%M:%S')
#HE WON IN SPA, HE WINS IN MONZA! CHARLES LECLERC IS THE WINNER OF 2019 ITALIAN GRAND PRIX!!! 
d2 = datetime.now()
print(date_diff_sec(d2, d1))