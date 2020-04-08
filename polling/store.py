"""
save messages to file when it reach to some value (ex. 10)
should call func save() on exception from serv
"""
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
