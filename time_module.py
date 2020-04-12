import time

print(time.gmtime())
# gmtime(secs) converts time in seconds since epoch to a sruct_time in UTC
# struct_time is a named tuple that contains 9 integers
# if secs is not specified, then current time as returned by time() is used.

print(time.localtime())
# like gmtime(), but converts to local time

print(time.mktime(time.localtime()))
# mktime() accepts localtime() and returns the floating point number representing seconds

print(time.asctime(time.localtime()))
print(time.asctime(time.gmtime()))
# asctime() accepts a tuple or struct_time and converts it to a formatted string

print(time.ctime(time.mktime(time.localtime())))
# ctime() accepts a time in seconds since epoch and converts it to a formatted string

print(time.strptime("30 Nov 00", "%d %b %y"))
# strptime() is used to parse a given string representing time in a specified format and convert it to a struct_time value

print(time.time())
# this returns the current time since epoch in seconds

