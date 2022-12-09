def solution(genres, plays):

    # 속한 노래가 많이 재생된 장르 정렬
    playsPerGenre = {}
    # {classic: [plays, {}], pop: [plays, {}]}
    # {'classic': [1450, {0: 500, 2: 150, 3: 800}], 'pop': [3100, {1: 600, 4: 2500}]}
    for i in range(len(genres)):
        if genres[i] in playsPerGenre:
            playsPerGenre[genres[i]][0] += plays[i]
            playsPerGenre[genres[i]][1][i] = plays[i]
        else:
            playsPerGenre[genres[i]] = [plays[i], {i : plays[i]}]
    
    # 장르 정렬
    playsPerGenre = sorted(playsPerGenre.items(), key=lambda genre:genre[1][0], reverse=True)
    
    # 노래 정렬
    for genre in playsPerGenre:
        genre[1][1] = sorted(genre[1][1].items(), key=lambda song:song[1], reverse=True)

    # 값 저장
    answer = []
    for genre in playsPerGenre:
        answer.append(genre[1][1][0][0])
        if len(genre[1][1]) > 1:
            answer.append(genre[1][1][1][0])
    
    return answer