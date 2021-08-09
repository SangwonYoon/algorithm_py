def solution(price, money, count):
    
    return count*(count+1)/2*price-money if money < count*(count+1)/2*price else 0