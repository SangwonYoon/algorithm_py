N = input()

half = len(N) // 2
if len(N) % 2 == 0:
    palindrom = N[:half] + N[half-1::-1]
elif len(N) == 1 and N != "9":
    palindrom = int(N) + 1
elif N == "9":
    palindrom = "11"
else:
    palindrom = N[:half] + N[half] + N[half-1::-1]

if int(palindrom) <= int(N):
    N = str(int(N) + int("1" + "0"*half))
    half = len(N) // 2
    if len(N) % 2 == 0:
        palindrom = N[:half] + N[half-1::-1]
    else:
        palindrom = N[:half] + N[half] + N[half-1::-1]
    
print(palindrom)
    