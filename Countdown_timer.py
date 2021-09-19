#COUNTDOWN TIMER
import time

def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        print(t)
        t -= 1
    print("Timer Completed")

t = input('Enter time in seconds: ')

countdown(int(t))
