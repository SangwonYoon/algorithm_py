def solution(number, k):
    i = 0
    while i < len(number):
        if i != 0 and int(number[i-1]) < int(number[i]):
            number = number[:i-1] + number[i:]
            k -= 1
            i -= 1
        elif i != len(number)-1 and int(number[i]) < int(number[i+1]):
            number = number[:i] + number[i+1:]
            k -= 1
        else:
            i += 1
        if k == 0:
            return number
    return number[:len(number)-k]