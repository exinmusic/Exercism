def leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True # Divisible by 4 but not 100
        else:
            return year % 400 == 0 # Divisible by 100 and 400
    else:
        return False

        
