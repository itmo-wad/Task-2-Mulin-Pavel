from flask import Flask, render_template
from flask_socketio import SocketIO
from flask import jsonify
from threading import Thread
import time
import Artificial_Intelligence
import store

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)




@app.route('/')
def sessions():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('user_send')
def handle_my_custom_event(json, methods='POST'):
    global message
    message = json['message']
    socketio.emit('my response', json, callback=messageReceived)
    store.store_messages(json['message'], 'user')

@socketio.on('bot_response')
def handle_my_request_event(methods='GET'):
    answer = Artificial_Intelligence.AI_answer(message)
    socketio.emit('bot response', answer, callback=messageReceived)
    store.store_messages(answer['message'], 'bot')

@socketio.on('bot_command')
def handle_my_command(methods='GET'):
    answer = {'message':'Use --help.'}
    message_list = message.split('--')
    if len(message_list) > 1:
        if message_list[1] == 'alive':
            answer = {'message':'** --- ***'}
            thread1 = Thread(target=bot_speaking)
            thread1.start()
        elif message_list[1] == 'poweroff':
            answer = {'message':'goodbye, my friend'}
        elif message_list[1] == 'cmatrix':
            answer = {'message':'csdgegbmerngmekjtnerinevrigunrg w'}
        elif message_list[1] == 'help':
            answer = {'message':'--alive        It alives the bot <br>--poweroff     It do nothing<br>--cmatrix      :)'}

    socketio.emit('bot response', answer)


def bot_speaking():
    time.sleep(5)
    dialog = ['hi', 'are you alone?', 'im very lonely', 'say something', 'i dont hear you', 'it was my fault', 'forgive me', 'say smth', 'please','i beg you', 'ok, good bye']
    for number in range(len(dialog)-1):
        socketio.emit('bot response', {"message": dialog[number]})
        time.sleep(1)


if __name__ == "__main__":
    try:
        socketio.run(app, debug=True)
    except Exception as e:
        print(e)
        print('why we here?')
        store.save()


thread1 = Thread(target=main)

thread1.start()
thread2.start()
