from collections import OrderedDict
ordered_dict = OrderedDict()
for _ in range(int(input())):
    key = input()
    ordered_dict[key] = ordered_dict.setdefault(key, 0) + 1
print(len(ordered_dict))    
print(*ordered_dict.values()) 
