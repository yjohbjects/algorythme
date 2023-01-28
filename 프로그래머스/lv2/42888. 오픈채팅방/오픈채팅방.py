def solution(record):
    answer = []

    db = {}
    log = []
    for rcd in record:
        msg = rcd.split(' ')
        if msg[0] == 'Enter' or msg[0] == 'Change':
            db[msg[1]] = msg[2]

        log.append([msg[0], msg[1]])

    for record in log: # [action, id]

        if record[0] == 'Enter':
            answer.append(f'{db[record[1]]}님이 들어왔습니다.')

        elif record[0] == 'Leave':
            answer.append(f'{db[record[1]]}님이 나갔습니다.')

    return answer