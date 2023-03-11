def solution(array):
    answer = 0
    freq = {}
    
    for num in set(array):
        freq[num] = array.count(num)
        
    if list(freq.values()).count(max(list(freq.values()))) > 1: 
        answer = -1
        
    else:
        for key in list(freq.keys()):
            if freq[key] == max(list(freq.values())):
                answer = key
            
        # answer = max(list(freq.values()))
        
    return answer