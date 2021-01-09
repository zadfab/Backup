start_time = input( "Enter the starting time")
end_time = input( "Enter the ending time")

start_time = start_time.split(":")
end_time = end_time.split(":")

start_minute = int(start_time[0])*60
end_minute = int(end_time[0])*60
print(start_minute,end_minute)
start_total = start_minute + int(start_time[1])
end_total = end_minute + int(end_time[1])
print(start_total,end_total)
print(end_total - start_total)

