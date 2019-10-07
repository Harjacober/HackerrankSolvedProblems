def swap_case(s):
    ans = [i.lower() if i.isupper() else i.upper() for i in s]  
    return ''.join(ans)

