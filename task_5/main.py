n = int(input())

minutes_in_day = 1440
minutes_in_hour = 60

x = n % minutes_in_day
hours = x // minutes_in_hour
minutes = x % minutes_in_hour

print(hours, minutes)
