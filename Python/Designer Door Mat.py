def doorMat(N, M):
    N = N//2
    pat = [(".|."*i+".|."+".|."*i).center(M,"-") for i in range(N)]
    print("\n".join(pat))
    print("WELCOME".center(M,"-"))
    print('\n'.join(pat[::-1]))


if __name__ == '__main__':
    inp = list(map(int, input().split()))
    N = inp[0]
    M = inp[1]
    doorMat(N, M)
