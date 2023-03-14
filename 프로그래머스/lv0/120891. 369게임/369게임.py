def solution(order):
    text = str(order)
    return text.count('3') + text.count('6') + text.count('9')