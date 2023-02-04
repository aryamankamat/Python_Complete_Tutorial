import time #The time() function in the time module returns the current time in seconds with millisecond precision elapsed since the time 00:00:00
current_time = time.time() # Get current time
#print(current_time)
totalSeconds = int(current_time) # Obtain the total seconds
#print(totalSeconds)
currentSeconds = totalSeconds % 60 # Get the current second
#print(currentSeconds)
totalMinutes = totalSeconds // 60 # Obtain the total minutes
#print(totalMinutes)
currentMinutes = totalMinutes % 60  # Compute the current minute in the hour
#print(currentMinutes)
totalHours = totalMinutes // 60 # Obtain the total hours
#print(totalHours)
currentHours = totalHours % 24 # Compute the current hour
#print(currentHours)
print("Current time is", currentHours, ":",currentMinutes, ":", currentSeconds, "GMT")
