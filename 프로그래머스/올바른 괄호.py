def solution(s):
    st = 0
    for i in s:
        if i == "(":
            st += 1
        elif i == ")":
            if st == 0:
                return False
            else:
                st -= 1
    
    if st == 0:
        return True
    return False