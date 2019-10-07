import string
def print_rangoli(size):
    # your code goes here
    l =[]
    alpha = string.ascii_lowercase
    for i in range(size):
        s = "-".join(alpha[i:size])
        l.append((s[::-1]+s[1::]).center(4*size-3,'-'))
    print('\n'.join(l[len(l):0:-1]+l))
