def solution(emergency):
    answer = []
    
    emergency_sorted = sorted(emergency, reverse=True)
    
    for patient in emergency:
        answer.append(emergency_sorted.index(patient) + 1)
    return answer