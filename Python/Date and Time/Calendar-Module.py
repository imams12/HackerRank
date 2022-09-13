# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

MM, DD, YYYY = map(int, input().split())
day = calendar.weekday(YYYY, MM, DD)

print(str(calendar.day_name[day].upper()))
