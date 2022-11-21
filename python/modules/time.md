# time
time() -  returns the number of seconds passed since epoch
ctime() - takes seconds passed since epoch as an argument and returns a string representing local time.
sleep() - suspends (delays) execution of the current thread for the given number of seconds.

- struct_time
time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, 
                    tm_hour=6, tm_min=35, tm_sec=17, 
                    tm_wday=3, tm_yday=361, tm_isdst=0)


- localtime() - takes the number of seconds passed since epoch as an argument and returns struct_time in local time.
- gmtime() - function takes the number of seconds passed since epoch as an argument and returns struct_time in UTC.
- mktime() - The mktime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument and returns the seconds passed since epoch in local time. Basically, it's the inverse function of localtime().

- asctime() - takes struct_time as argument and return string representing it

- strftime() - take formated string and struct_time and return time string
eg. time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

- strptime()

