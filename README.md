# Sleep Schedule Correction Program

This program helps users correct their sleep schedule over a specified period by calculating an ideal path to a fixed circadian cycle.

## Features

- **User Input:**
  - Takes input for the current sleep time, the desired correction time, and the number of days for the correction.

- **Efficiency Calculation:**
  - Determines whether it's more efficient to add or subtract hours to reach the desired sleep schedule.

- **Schedule Generation:**
  - Creates a daily schedule for the specified correction period.

## Requirements

- Python 3.x
- colorama library (install using `pip install colorama`)

## Usage

1. Run the program.
2. Enter the current sleep time when prompted.
3. Enter the desired sleep schedule time.
4. Specify the number of days for the correction.

The program will then calculate the most efficient way to adjust the sleep schedule and provide a daily plan.


## How to Run

```bash
python sleepcalculator.py
```

## Example 
```
| Current sleep time?: 23:00
| What time would you like to correct to?: 07:00
| How many days to correct?: 7
```
## Output
```
-- Subtracting hours is more efficient --
--------------------
Day     Time
--------------------
Day 0   11:00 PM
Day 1   10:00 PM
Day 2   09:00 PM
Day 3   08:00 PM
Day 4   07:00 PM
Day 5   06:00 PM
Day 6   05:00 PM
Day 7   04:00 PM
------------------------------
```