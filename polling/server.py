from flask import Flask, render_template, Response
from flask import request
from flask_cors import CORS
from flask import jsonify
import time
import Artificial_Intelligence
import store

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
#socketio = SocketIO(app)
CORS(app)

messages = []
bot_speaking = False
dialog = ['hi', 'are you alone?', 'im very lonely', 'say something', 'i dont hear you', 'it was my fault', 'forgive me', 'say smth', 'please','i beg you', 'ok, good bye']
dialog.reverse()

@app.route('/')
def sessions():
    return render_template('index.html')

@app.route('/messageandanswer', methods=['GET', 'POST'])
def receive_and_answer():
    return jsonify({"msg":"answer"})

@app.route('/message', methods=['POST'])
def receiving_message():
    global messages
    msg = request.data.decode("utf-8")
    messages.append(msg)
    store.store_messages(msg, 'user')
    return "received"

@app.route('/answer', methods=['GET'])
def polling():
    global messages
    global bot_speaking
    try:
        time.sleep(1)
        message = messages.pop()
        if message == "alive":
            answer = "ok!"
            bot_speaking = True
        else:
            answer = Artificial_Intelligence.AI_answer(message)
            store.store_messages(answer, 'bot')
    except IndexError:
        if bot_speaking:
            answer = bot_speak()
            if answer == "finish":
                answer = "200OK"
        else:
            answer = "200OK"
    print(answer)
    return jsonify({'message':answer})



def bot_speak():
    global dialog
    global bot_speaking
    try:
        answer = dialog.pop()
    except IndexError:
        bot_speaking = False
        answer = "finish"
    return answer


if __name__ == "__main__":
    try:
        app.run(host='localhost',port=5000, threaded = True, debug=True)
    except Exception as e:
        print(e)
        print('why we here?')
        store.save()
