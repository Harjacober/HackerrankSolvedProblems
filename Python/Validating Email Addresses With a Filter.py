import re
def fun(s):
    pattern = re.compile(r'[\w-]+@[A-Za-z0-9]+\.[A-za-z]{1,3}$')
    return bool(re.match(pattern, s))
    # return True if s is a valid email, else return False
