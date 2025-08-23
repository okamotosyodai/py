N, X, Y = map(int, input().split())

for p in range(1,N+1):
    if p % X == 0 and p % Y == 0:
        print('AB')
    elif p % X == 0:
        print('A')
    elif p % Y == 0:
        print('B')
    else:
        print('N')
