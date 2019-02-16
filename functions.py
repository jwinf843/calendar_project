from utils import DAYS_PER_MONTH
from utils import MONTH_ORDER
from utils import DAYS_OF_WEEK

DEBUG = True

def leap_year_check(year):
    if year % 4 == 0:
        return True
    
assert leap_year_check(2020) == True
assert leap_year_check(2019) == None
if DEBUG:
    print('Leap year check passed')
    
def create_calendar_month(month, first_day):
    # 'Feb 1, Monday: []'
    month_dictionary = {}
    index = DAYS_OF_WEEK.index(first_day)
    DAY_RANGE = DAYS_PER_MONTH[month] + 1
    for day in range(1, DAY_RANGE):
        abb = month[:3]
        index %= 7
        day_of_week = DAYS_OF_WEEK[index]
        key = '{} {}, {}'.format(abb, day, day_of_week)
        month_dictionary.setdefault(key, [])
        index += 1
    
    print(month_dictionary)
    return month_dictionary

FEB = create_calendar_month('February', 'Friday')
assert FEB['Feb 1, Friday'] == []
assert FEB['Feb 28, Thursday'] == []
assert len(FEB) == 28
if DEBUG:
    print('create_calendar_month check passed')

def create_calendar_year(year, first_day):
    if leap_year_check == True:
        pass
    calendar_year = []
    
    for month in MONTH_ORDER:
        pass
        
# create_calendar(2019, 'Tuesday')