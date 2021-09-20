#1107번

N = int(input()) #목적 채널
M = int(input()) #고장난 버튼 개수
if M != 0:
    crashedBtn = list(map(int,input().split())) #고장난 버튼 리스트
else:
    crashedBtn = list()

offset = 0
while(True):
    target = N - offset if N - offset >= 0 else 0
    if target == 100:
        print(offset)
        break
    else:
        for i in str(target):
            if int(i) in crashedBtn:
                break
        else:
            print(min(len(str(target)) + offset,abs(100-N)))
            break
    target = N + offset
    if target == 100:
        print(offset)
        break
    else:
        for i in str(target):
            if int(i) in crashedBtn:
                break
        else:
            print(min(len(str(target)) + offset,abs(100-N)))
            break
    offset += 1