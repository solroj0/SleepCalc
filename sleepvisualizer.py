from datetime import datetime, timedelta
from colorama import Fore, Style

def get_time_input(prompt):
    formats = ["%H:%M", "%H", "%I:%M %p", "%I %p"]
    while True:
        start = input(prompt)
        for fmt in formats:
            try:
                return datetime.strptime(start.upper(), fmt) 
            except ValueError:
                pass
        print("Invalid input. Enter time in HH:MM, HH, HHAM, or HH:MM AM/PM.")

def find_efficient_direction(start, goal):
    goalminus = goal - timedelta(days=1)
    added = goal - start
    subtract = start - goalminus

    # Compare absolute values
    if abs(added) < abs(subtract):
        print("-- Adding hours is more efficient --")
        print("-" * width)
        return "add", added
    else:
        print("-- Subtracting hours is more efficient --")
        print("-" * width)
        return "subtract", subtract

def create_schedule(operation, time_difference, time_interval):
    schedule = [[f"0", start.strftime("%I:%M %p")]]
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

def simple_vis(schedule):
    vis = []
    max_vis_length = 48

    for item in schedule[0:]:
        # Convert the string to a datetime object
        item_time = datetime.strptime(item[1], "%I:%M %p")

        # Calculate the ratio considering additional characters in the visualization
        ratio = int((item_time.hour * 60 + item_time.minute) / (24 * 60) * (max_vis_length - 4))

        # Format the visualization string with proper padding
        vis.append("|" + " " * 2 + " " * ratio + "--" + " " * (max_vis_length - ratio - 4) + "|")

    return vis


def print_results(schedule):
    print(f"{'  Day':<6}{'  Time':<9}{'Visualization':>26}")
    
    # Print the header row with numbers 2, 4, 6, up to 24
    clock = [12,2,4,6,8,10,12,2,4,6,8,10]
    print("|" + " " * 14 + "|" + "".join([f"{i:<4}" for i in clock]) + "|")

    for i, item in enumerate(schedule):
        print(f"|{item[0]:>3}  {item[1]} {simple_vis(schedule)[i]}")
    print("-" * width + Style.RESET_ALL)




width = 80 
print(Fore.GREEN + "-" * width)
print("- Let's calculate the ideal path to a fixed circadian cycle -")
start = get_time_input("| Current sleep time?: ")
goal = get_time_input("| What time would you like to correct to?: ")
time_interval = int(input("| How many days to correct?: "))

operation, time_difference = find_efficient_direction(start, goal)
schedule = create_schedule(operation, time_difference, time_interval)
print_results(schedule)
