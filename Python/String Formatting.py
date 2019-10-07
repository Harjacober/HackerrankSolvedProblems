def print_formatted(number):
    # your code goes here
    w = len(format(number, 'b'))
    for i in range(1,number+1):
        print("{0:{1}d} {0:{1}o} {0:{1}x} {0:{1}b}".format(i,w).upper())

