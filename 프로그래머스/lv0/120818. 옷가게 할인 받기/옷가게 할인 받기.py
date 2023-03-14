import math

def solution(price):
    if price >= 500000:
        return math.floor(price * 0.8)
    elif price >= 300000:
        return math.floor(price * 0.9)
    elif price >= 100000:
        return math.floor(price * 0.95)
    else:
        return price