from itertools import groupby
s = list(map(int, input()))
ans = [(len(list(iterator)),each) for each, iterator in groupby(s)]
print(*ans)
