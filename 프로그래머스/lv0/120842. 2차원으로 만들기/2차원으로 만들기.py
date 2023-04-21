def solution(num_list, n):
    answer = []    
    
    for i in range(0, len(num_list) - n + 1, n):
        temp = []
        for j in range(n):
            temp.append(num_list[i + j])
        answer.append(temp)
        
    return answer