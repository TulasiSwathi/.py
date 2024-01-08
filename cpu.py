import os.path

# Read first line from /proc/stat. It should start with "cpu"
# and contains times spent in various modes by all CPU's totalled.
#
with open("/proc/stat") as procfile:
    cpustats = procfile.readline().split()

# Sanity check
#
if cpustats[0] != 'cpu':
    raise ValueError("First line of /proc/stat not recognised")

#
# Refer to "man 5 proc" (search for /proc/stat) for information
# about which field means what.
#
# Here we do calculation as simple as possible:
# CPU% = 100 * time_doing_things / (time_doing_things + time_doing_nothing)
#

user_time = int(cpustats[1])    # time spent in user space
nice_time = int(cpustats[2])    # 'nice' time spent in user space
system_time = int(cpustats[3])  # time spent in kernel space

idle_time = int(cpustats[4])    # time spent idly
iowait_time = int(cpustats[5])    # time spent waiting is also doing nothing

time_doing_things = user_time + nice_time + system_time
time_doing_nothing = idle_time + iowait_time

# The times read from /proc/stat are total times, i.e. *all* times spent
# doing things and doing nothing since last boot.
#
# So to calculate  meaningful CPU % we need to know how much these values
# have *changed*.  So we store them in a file which we read next time the
# script is run.
# 
previous_values_file = "/tmp/prev.cpu"
prev_time_doing_things = 0
prev_time_doing_nothing = 0

try:
    with open(previous_values_file) as prev_file:
        prev1, prev2 = prev_file.readline().split()
    prev_time_doing_things = int(prev1)
    prev_time_doing_nothing = int(prev2)
except IOError:  # To prevent error/exception if file does not exist. We don't care.
    pass   

# Write the new values to the file to use next run
#
with open(previous_values_file, 'w') as prev_file:
    prev_file.write("{} {}\n".format(time_doing_things, time_doing_nothing))

# Calculate difference, i.e: how much the number have changed
#
diff_time_doing_things = time_doing_things - prev_time_doing_things
diff_time_doing_nothing = time_doing_nothing - prev_time_doing_nothing

# Calculate a percentage of change since last run:
#
cpu_percentage = 100.0 * diff_time_doing_things/ (diff_time_doing_things + diff_time_doing_nothing)

# Finally, output the result
#
print ("CPU", cpu_percentage, "%")
