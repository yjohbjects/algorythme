def solution(numer1, denom1, numer2, denom2):
    temp = ((numer1 / denom1) + (numer2 / denom2))
    
    
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    for i in range(2, max(numer, denom)):
        while numer % i == 0 and denom % i == 0:
            numer, denom = numer // i, denom // i
    
    answer = [numer, denom]    
    
    print(answer)
    return answer