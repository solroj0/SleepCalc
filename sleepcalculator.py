"""
This program is an attempt to correct a user's sleep schedule 
The goal is to create a plan to adjust the sleeping times in a set period
"""
from datetime import datetime, timedelta
from colorama import Fore, Style

def get_time_input(prompt):
    formats = ["%H:%M", "%H", "%I:%M %p", "%I %p"] #check common time formats
    while True:
        start = input(prompt)
        for fmt in formats:
            try:
                return datetime.strptime(start.upper(), fmt) 
            except ValueError:
                pass
        print("Invalid input. Enter time in HH:MM, HH, HHAM, or HH:MM AM/PM.")

def find_efficient_direction(start, goal):
    goalminus = goal  - timedelta(days=1)
    added     = goal  - start
    subtract  = start - goalminus

    # Compare absolute values
    if abs(added) < abs(subtract):
        print("-- Adding hours is more efficient --")
        print("-" * 60)
        return "add", added
    else:
        print("-- Subtracting hours is more efficient --")
        print("-" * 60)
        return "subtract", subtract

def create_schedule(operation, time_difference, time_interval):
    schedule = [[f"0", start.strftime("%I:%M %p")]] #initiate list 
    time_perday = time_difference / time_interval    
    time_step = start
    
    if operation == "add":
        for x in range(time_interval):
            time_step = time_step + time_perday
            schedule.append([f"{x+1}", time_step.strftime("%I:%M %p")])
        return schedule
    elif operation == "subtract":
        for x in range(time_interval):
            time_step = time_step - time_perday
            schedule.append([f"{x+1}", time_step.strftime("%I:%M %p")])
        return schedule
    
def print_results(schedule):
    print(f"{'  Day':<6}{'  Time':<12}")
    for item in schedule:
        print(f"{Fore.GREEN}|{Fore.YELLOW}{item[0]:>3}  {item[1]}{Fore.GREEN} |")    
    print(Fore.GREEN + "-" *60 + Style.RESET_ALL)

# init(autoreset=True) #to autoreset colors
print(Fore.GREEN + "-"*60)
print("| Let's calculate the ideal path to a fixed circadian cycle ")
start = get_time_input("| Current sleep time?: ")
goal = get_time_input("| What time would you like to correct to?: ")
time_interval = int(input("| How many days to correct?: "))

operation, time_difference = find_efficient_direction(start, goal)
schedule = create_schedule(operation, time_difference, time_interval)
print_results(schedule)