import time # import time module to work with time-related functions
import sys # import sys module to access system-specific parameters and functions
import os # import os module to access operating system functionality
import signal # import signal module to handle signals

print(f"\n{'='*80}\n{'Countdown Timer':^80}\n{'='*80}\n") # print a formatted header for the countdown timer

seconds = int(input("Enter the number of seconds for the countdown timer: ")) # prompt user to input the number of seconds for the countdown timer

while seconds >= 0: # loop until seconds is greater than or equal to 0
    mins, secs = divmod(seconds, 60) # calculate minutes and seconds from total seconds
    
    timer = '{:02d}:{:02d}'.format(mins, secs) # format the timer string as MM:SS
    print(timer, end="\r") # print the timer string and overwrite the previous line
    
    # Autre écriture pour les lignes 13 et 14
    # print(f"{mins:02d}:{secs:02d}", end="\r") # alternative way to format and print the timer string
    
    time.sleep(1) # wait for 1 second
    seconds -= 1 # decrement the seconds by 1
    
print("Time's up!") # print "Time's up!" when the countdown reaches 0

print(f"\n{'='*80}\n")
