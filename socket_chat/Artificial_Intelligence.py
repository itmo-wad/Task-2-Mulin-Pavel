

greeting = ['hello', 'hi']
weather = ['weather']
howareyou = ['how', 'what', 'could']
doingsmth = ['set', 'get', 'find', 'look']




def AI_answer(user_message):
    answer = {'message':"Sorry, i don't understand you.:("}
    print(user_message)
    print(type(user_message))
    lower_umessage = user_message.lower()
    words = lower_umessage.split(' ')
    if len(words) > 1:
        for message in words:
            if message in greeting:
                answer['message'] = 'Hello, human!'
                break
            elif message in weather:
                answer['message'] = 'Such a lot of viruses outside. Home is better!'
                break
            elif message in howareyou:
                answer['message'] = 'Im just a robot, lets talk about you, how are you?'
                break
            elif message in doingsmth:
                answer['message'] = 'I have not a permission for that'
                break
    else:
        if words[0] in greeting:
            answer['message'] = 'Hello, human!'
        elif words[0] in weather:
            answer['message'] = 'Such a lot of viruses outside. Home is better!'
        elif words[0] in howareyou:
            answer['message'] = 'Not bad, lets talk about you, how are you?'
        elif words[0] in doingsmth:
            answer['message'] = 'I have not a permission for that'
    return answer
