import datetime

def add(moment):
    moment += datetime.timedelta(seconds=1000000000)
    return moment
    
