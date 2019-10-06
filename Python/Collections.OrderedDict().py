from collections import OrderedDict
ordered_dict = OrderedDict()
for _ in range(int(input())): 
    key, _, value = input().rpartition(' ')
    ordered_dict[key] = ordered_dict.setdefault(key,0) + int(value)
print(*(f"{key} {val}" for key,val in ordered_dict.items()), sep="\n")
