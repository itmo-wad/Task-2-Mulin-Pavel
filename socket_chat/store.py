


all_messages = ''


def store_messages(message, speaker):
    global all_messages
    all_messages += speaker+':'+message+'\n'
    if len(all_messages.split('\n')) > 10:
        file = open('history.txt', 'a')
        file.write(all_messages)
        file.close()


def save():
    file = open('history.txt', 'a')
    file.write(all_messages)
    file.close()



check = '--dfgdfg'

check2 = 'hui'

print(check.split('--'))
print(check2.split('--'))
