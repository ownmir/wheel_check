#
import sys
import datetime
from pytz import timezone

now = datetime.datetime.now(timezone('Europe/Kiev'))
# print('now', now)
# print('now.year', str(now.year))
# print('now.month', str(now.month))
# print('now.day', str(now.day))
logfilestr = 'Info-' + str(now.year) + str(now.month) + str(now.day) + '.log'
# with open(logfilestr, 'w', encoding='utf-8') as create:
#     for i in range(1, 10):
#         create.write('------------' + datetime.datetime(2019, 10, 11, 11, 49 + i).strftime('%H:%M') + '\n')
#     # create.write('')
# with open(logfilestr, 'r', encoding='utf-8') as log:
#     for line in log:
#         print('Line', line)
#         last_time = line[12:17]
#         print('Time:', last_time)
#     try:
#         print('Last time:', last_time)
#     except NameError:
#         print('File is empty')
#         sys.exit()
#     try:
#         hour = int(last_time[0:2])
#         print('Last hour:', hour)
#     except:
#         print('err hour')
#         sys.exit()
#     try:
#         minute = int(last_time[3:5])
#         print('Last minute:', minute)
#     except:
#         print('err minute')
#         sys.exit()

# time0 = datetime.datetime(2019, 10, 11, 10, 0)
# print('time0', time0)
# time5 = datetime.datetime(2019, 10, 11, 10, 5)
# print('time5', time5)
# diff5 = time5 - time0
# print('diff5.total_seconds', diff5.total_seconds())

# inlog = datetime.datetime(now.year, now.month, now.day, hour - 3, minute, 0).astimezone(timezone('Europe/Kiev'))
# print('inlog', inlog)
# diff = now - inlog
# print('diff.total_seconds', diff.total_seconds())
# diff_seconds = diff.total_seconds()
# if diff_seconds > 0 and diff_seconds > 300:
#     print('diff_seconds > 0 and diff_seconds > 300 !!!')
# print('diff day', diff.days)

# Читаю из сквидовского аксесс лога последнюю строчку так:

# blk_size = 4096
# fp = open('blablabla.txt', 'rb')
# fp.seek(-blk_size, 2)
# raw_data = fp.read()
# fp.close()
# last_line = raw_data.split('\n')[-2]