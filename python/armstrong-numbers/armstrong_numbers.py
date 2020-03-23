def is_armstrong_number(number):
    digits = [ int(i) for i in str(number) ]
    powers = [ x ** len(digits) for x in digits ]
    return sum(powers) == number