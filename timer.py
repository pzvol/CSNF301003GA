import time


#### Code for timer ####

# Variable for storing recorded timestamp
timer_record = 0

# Method for updating timer (setting the starting time)
def timer_start():
	global timer_record
	timer_record = time.time()

# Method for printing the time since last update
#
# the second num will be returned
def timer_read(print_result=True):
	second_passed = time.time() - timer_record
	if print_result:
		print(f"{second_passed:.3}s passed")
	return second_passed



#### Example of using ####

timer_start()     # Start the timer
time.sleep(2.54)  # Sleep for a specific duration (2.54s)

timer_read()      # Print the timer
# output: 2.55s passed

# Alternatively, you can record the number of time and print it yourself
timer_number=timer_read(False)
print(f"{timer_number} was returned by `timer_read` and printed by myself")
