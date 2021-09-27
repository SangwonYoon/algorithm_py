#10816번

import sys
input = sys.stdin.readline

def binSearch(s,e,target):
    if s > e:
        return 0
    mid = (s+e) // 2
    if sorted_cards[mid][0] == target:
        return sorted_cards[mid][1]
    elif sorted_cards[mid][0] > target:
        return binSearch(s,mid-1,target)
    else:
        return binSearch(mid+1,e,target)

N = int(input())
arr = list(map(int,input().split()))
cards = dict() 
for i in arr:
    if(i in cards):
        cards[i] += 1
    else:
        cards[i] = 1
M = int(input())
check = list(map(int,input().split()))
answer = [0] * len(check)

sorted_cards = sorted(cards.items()) #딕셔너리를 key값을 기준으로 정렬, 리턴값은 리스트 안에 키, 값쌍이 튜플로 들어 있는 형식
for i in range(len(check)):
    answer[i] = binSearch(0,len(sorted_cards)-1,check[i])

for i in answer:
    print(i, end=" ")
