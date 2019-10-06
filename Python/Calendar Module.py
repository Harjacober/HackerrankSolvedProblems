import calendar# Enter your code here. Read input from STDIN. Print output to STDOUT
mm, dd, yyyy = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(yyyy, mm, dd)].upper()) 
