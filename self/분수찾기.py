# 1193번

X = int(input())

diag = 1
while X > diag:
    X -= diag
    diag += 1

if diag % 2 == 0:
    print(f"{X}/{diag+1-X}")
else:
    print(f"{diag+1-X}/{X}")
