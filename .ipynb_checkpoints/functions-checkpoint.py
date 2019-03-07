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
    
#     print(month_dictionary)
    return month_dictionary

JAN = create_calendar_month('January', 'Tuesday')
FEB = create_calendar_month('February', 'Friday')
assert FEB['Feb 1, Friday'] == []
assert FEB['Feb 28, Thursday'] == []
assert len(FEB) == 28
if DEBUG:
    print('create_calendar_month check passed')
     
def get_first_day(month):
    last_day = None
    
    for day in month: 
        date = day.split(' ')
        date_num = date[1]
        date_num = date_num[:-1]
        print(date_num)
        if int(date_num) == len(month):
            last_day = date[2]
    
    index = DAYS_OF_WEEK.index(last_day) + 1
    index %= 7            
    first_day = DAYS_OF_WEEK[index]
    
    return first_day

assert get_first_day(JAN) == 'Friday'
assert get_first_day(FEB) == 'Friday'
if DEBUG:
    print('First Day Check Passed')
    
def create_calendar_year(year, first_day):
    if leap_year_check(year) == True:
        DAYS_PER_MONTH['February'] = 29
    else:
        DAYS_PER_MONTH['February'] = 28
    
    calendar_year = []
    
    for month in MONTH_ORDER:
        build_month = create_calendar_month(month, first_day)
        calendar_year.append(build_month)
        first_day = get_first_day(build_month)
        
    return calendar_year

print(create_calendar_year(2019, 'Tuesday'))
