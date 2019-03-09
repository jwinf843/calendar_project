from functions import create_calendar_year, add_task, parse_month

y2019 = create_calendar_year(2019, 'Tuesday')

def view_calendar():
    print('View [Y]ear')
    print('View [M]onth')
    user_input = input('Please select a viewing option: ').lower()
    
    if user_input == 'y':
        print(y2019)
        
    elif user_input == 'm':
        user_month = input('Select a month to view: ').lower()
        month = parse_month(user_month)
        
        for day, events in y2019[month].items():
            if events != []:
                print(day, events)
        

def start_menu(): 
    print('[V]iew Calendar')
    print('[A]dd Task')
    user_input = input('Choose an option: ').lower()
    
    if user_input == 'v':
        print('You have selected to view calendar')

    if user_input == 'a':
        print('You have selected to add a task')
        
    start_menu()

start_menu()