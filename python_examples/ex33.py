def add_amount_to_list(num):
    numbers = []
    i = 0
    while i < num:
        numbers.append(i)
        i += 1
    print "The numbers are: %r" % numbers
    return numbers


add_amount_to_list(6)
