import telebot
from flask import Flask, render_template, request
from threading import Thread

app = Flask(__name__)

telebot.apihelper.proxy = {'https': 'socks5://tvorogme@tvorog.me:6666'}

token = '632107141:AAEy6F1g3ZxJj1q7-kqCv-ltuvsdw-HDXGk'

bot = telebot.TeleBot(token=token)

words = []

@bot.message_handler(content_types=['text'])
def echo(message):
        global words
        text = message.text
        user = message.chat.id
        txt = text
        words.append(txt)


@app.route('/')
def index():
    global words
    return render_template('otpr.html', text = words)

def polling():
    bot.polling(none_stop=True)

polling_thread = Thread(target=polling)
polling_thread.start()
app.run(debug=True, port=8080)