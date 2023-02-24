def solution(sizes):
    
    max_width = 0
    max_height = 0
    
    for card in sizes:
        if card[0] >= card[1]:
            width = card[0]
            height = card[1]
        else:
            width = card[1]
            height = card[0]
            
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height
            
    answer = max_width * max_height
    return answer