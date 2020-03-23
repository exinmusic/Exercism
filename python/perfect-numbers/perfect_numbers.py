def classify(number):
    if number <= 0          : raise ValueError('Input was 0 or below.')
    aliquot = sum([ x for x in range(1,number) if number % x == 0 ])
    if aliquot == number    : return 'perfect'
    elif aliquot > number   : return 'abundant'
    else                    : return 'deficient'