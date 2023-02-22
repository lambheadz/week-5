from datetime import datetime, timedelta, timezone
today = datetime.now()
print(today)
thatday = today - timedelta(5)
tmz = today.strftime("%Z")
print(thatday)
print(tmz)