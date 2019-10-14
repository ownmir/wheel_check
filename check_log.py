import os, shutil, sys, datetime
from main import now, logfilestr
from pytz import timezone
import winsound


def write_error(message):
    with open('error.txt', 'w', encoding='utf-8') as no:
        no.write(message)


file_source = 'D:\\TOSS_SDO\\CorpLight\\logs\\' + logfilestr
if not os.path.exists(file_source):
    print('Log file does not exists!')
    write_error('Log file does not exists!')
    frequency = 2500
    duration = 2000
    winsound.Beep(frequency, duration)
    sys.exit()
file_target = 'D:\\TOSS_SDO\\CorpLight\\Check\\' + logfilestr
logfilestrcheck = shutil.copy2(file_source, file_target)
with open(logfilestrcheck, 'r', encoding='utf-8') as log:
    for line in log:
        # print('Line', line)
        last_time = line[12:17]
        # print('Time:', last_time)
    try:
        print('Last time:', last_time)
    except NameError:
        print('File is empty')
        write_error('File is empty')
        sys.exit()
    try:
        hour = int(last_time[0:2])
        # print('Last hour:', hour)
    except:
        print('err hour')
        write_error('err hour')
        sys.exit()
    try:
        minute = int(last_time[3:5])
        # print('Last minute:', minute)
    except:
        print('err minute')
        write_error('err minute')
        sys.exit()

# time0 = datetime.datetime(2019, 10, 11, 10, 0)
# print('time0', time0)
# time5 = datetime.datetime(2019, 10, 11, 10, 5)
# print('time5', time5)
# diff5 = time5 - time0
# print('diff5.total_seconds', diff5.total_seconds())

inlog = datetime.datetime(now.year, now.month, now.day, hour, minute, 0).astimezone(timezone('Europe/Kiev'))
print('now:', now)
print('time in log:', inlog)
diff = now - inlog
print('different in seconds', diff.total_seconds())
diff_seconds = diff.total_seconds()
if diff_seconds < 0:
    print('Tomorrow log??')
    write_error('Tomorrow log??')
if diff_seconds > 0 and diff_seconds > 300:
    print('diff_seconds > 0 and diff_seconds > 300 !!!')
    write_error('Different in seconds more then 300 !!!')
    frequency = 2500
    duration = 2000
    winsound.Beep(frequency, duration)
