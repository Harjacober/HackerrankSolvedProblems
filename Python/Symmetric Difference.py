M = input()
m = set(list(map(int, input().split())))
N = input()
n = set(list(map(int, input().split())))
print(*sorted(m.symmetric_difference(n)), sep="\n")
