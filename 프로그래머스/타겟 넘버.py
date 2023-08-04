answer = 0

def calculate(numbers, target, acc, idx, is_plus):
    global answer
    if is_plus:
        acc += numbers[idx]
    else:
        acc -= numbers[idx]
    
    if idx == len(numbers)-1:
        if acc == target:
            answer += 1
        return
    
    calculate(numbers, target, acc, idx+1, True)
    calculate(numbers, target, acc, idx+1, False)

def solution(numbers, target):
    calculate(numbers, target, 0, 0, True)
    calculate(numbers, target, 0, 0, False)
    return answer