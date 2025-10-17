from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date
    
def calculate_future_date(current_date):
    
    number = int(input("Enter the number of days to add to the current date:"))
    future_date = current_date + datetime.timedelta(days=number)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("future date: ", formatted_future)


current = display_current_datetime()
calculate_future_date(current)