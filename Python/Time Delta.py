from datetime import datetime, timedelta

# Complete the time_delta function below.
def time_delta(t1, t2):
    date1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    timedelta = abs(date2-date1) 
    return str(int(timedelta.total_seconds()))
