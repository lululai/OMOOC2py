import time

def change_time_format(string, format_from, format_to):
    temp_struct_time = time.strptime(string, format_from)
    output = time.strftime(format_to, temp_struct_time)
    return output

current_time = time.ctime() #return currnt time as a '%a %b %d %H:%M:%S %Y' format string
changed_time = change_time_format('Fri Oct 16 10:59:33 2015', '%a %b %d %H:%M:%S %Y', '%d/%m/%Y %H:%M:%S')
print "Current time is, ", changed_time