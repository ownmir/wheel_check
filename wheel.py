import datetime, time
from pytz import timezone
import threading


def loop():
    now = datetime.datetime.now(timezone('Europe/Kiev'))
    logfilestr = 'D:\\TOSS_SDO\\CorpLight\\logs\\Info-' + str(now.year) + str(now.month) + str(now.day) + '.log'

    time_work = 0
    # for i in range(1, 10):
    while True:
        with open(logfilestr, 'w', encoding='utf-8') as create:
            print('File', logfilestr, 'is opened')

            print('time_work', time_work)
            now = datetime.datetime.now(timezone('Europe/Kiev'))
            create.write('------------' + datetime.datetime(int(now.year), int(now.month), int(now.day), int(now.hour),
                                                            int(now.minute)).strftime('%H:%M') + ' time ' +
                         str(time_work) + '\n')
        time.sleep(5)
        time_work += 5


""""""
pot = threading.Thread(target=loop, daemon=True)
pot.start()
input('Press <Enter> to exit.\n')
# pot.join()

