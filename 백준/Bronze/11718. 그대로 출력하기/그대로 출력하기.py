while True:
    try:
        answer = input()
        print(answer)
    except EOFError:
        break