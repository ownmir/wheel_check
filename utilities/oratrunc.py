import datetime
from pytz import timezone


class ModeError(Exception):
    def __init__(self, text):
        self.txt = text


def oracle_trunc(current, mode):
    if mode == 'DAY':
        num_week_day = now.isoweekday()
        if num_week_day == 1:
            return current
        elif num_week_day == 2:
            return current - datetime.timedelta(days=1)
        elif num_week_day == 3:
            return current - datetime.timedelta(days=2)
        elif num_week_day == 4:
            return current - datetime.timedelta(days=3)
        elif num_week_day == 5:
            return current - datetime.timedelta(days=4)
        elif num_week_day == 6:
            return current - datetime.timedelta(days=5)
        elif num_week_day == 7:
            return current - datetime.timedelta(days=6)
        else:
            return current
    else:
        raise ModeError('Unknown mode!')



def oracle_addition(current, mode):
    if mode == 'DAY':
        num_week_day = now.isoweekday()
        if num_week_day == 1:
            return current + datetime.timedelta(days=6)
        elif num_week_day == 2:
            return current + datetime.timedelta(days=5)
        elif num_week_day == 3:
            return current + datetime.timedelta(days=4)
        elif num_week_day == 4:
            return current + datetime.timedelta(days=3)
        elif num_week_day == 5:
            return current + datetime.timedelta(days=2)
        elif num_week_day == 6:
            return current + datetime.timedelta(days=1)
        elif num_week_day == 7:
            return current
        else:
            return current
    else:
        raise ModeError('Unknown mode!')


if __name__ == '__main__':
    now = datetime.datetime.now(timezone('Europe/Kiev'))
    number_week_day = now.isoweekday()
    print('Hello from oratrunc! now', now, 'now.isoweekday()', number_week_day)
    date1 = oracle_trunc(now, 'DAY')
    print('date1', date1)
    if number_week_day in (1, 2, 3, 4):
        date2 = oracle_addition(now, 'DAY')
        print('date2', date2)
    elif number_week_day in (5, 6, 7):
        date2 = oracle_addition(now + datetime.timedelta(days=3), 'DAY')
        print('date2', date2)


