A = set(input().split())
n = int(input())
print(all([A>set(input().split())for _ in range(n)]))
