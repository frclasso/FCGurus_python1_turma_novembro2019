import datetime

data_str = 'July, 26, 2016'
dt = datetime.datetime.strptime(data_str, '%B, %d, %Y').date()
print(dt)