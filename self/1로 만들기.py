#1463번

def calc(num):
    if num % 3 == 0 and num % 2 == 0:
        mem.append(min(mem[num//3]+1, mem[num//2]+1, mem[num-1]+1))
    elif num % 3 == 0 and num % 2 != 0:
        mem.append(min(mem[num//3]+1, mem[num-1]+1))
    elif num % 3 != 0 and num % 2 == 0:
        mem.append(min(mem[num//2]+1, mem[num-1]+1))
    else:
        mem.append(mem[num-1]+1)

N = int(input())
mem = [0,0,1,1]
for i in range(4,N+1):
    calc(i)
print(mem[N])