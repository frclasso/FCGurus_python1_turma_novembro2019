from datetime import datetime
import pytz

local = datetime.now()
print(f'Local: {local.strftime("%m/%d/%Y, %H:%M:%S %p")}')

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print(f'New York: {datetime_NY.strftime("%m/%d/%Y, %H:%M:%S %p")}')

tz_london = pytz.timezone('Europe/London')
datetime_Londom = datetime.now(tz_london)
print(f'New York: {datetime_Londom.strftime("%m/%d/%Y, %H:%M:%S %p")}')

print()
# saber todas as zonas
for timezone in pytz.all_timezones:
    print(timezone)
