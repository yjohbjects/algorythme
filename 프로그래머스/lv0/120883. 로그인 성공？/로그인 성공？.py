def solution(id_pw, db):
    answer = ''
    
    db_dict = {}
    for item in db:
        db_dict[item[0]] = item[1]
        
    if id_pw[0] in db_dict:
        if id_pw[1] == db_dict.get(id_pw[0]):
            return 'login'
        else:
            return 'wrong pw'
    
    else:
        return 'fail'
    