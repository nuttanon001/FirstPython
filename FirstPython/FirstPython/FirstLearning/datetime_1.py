import datetime
#Print Date Now
print(datetime.datetime.now())
#Set datetime
dt = datetime.datetime(2016,10,21)
print(dt);
#Time delta
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
#Total seconds
print('Total Sec:',delta.total_seconds())
#delta string
print('String delta:',str(delta))
#Date to string
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%d/%m/%Y %H:%M:%S'))
#Converting Strings into datetime Objects
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))