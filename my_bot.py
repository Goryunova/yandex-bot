from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from telegram import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv()
secret_token = os.getenv('TOKEN')
updater = Updater(token=secret_token)

def say_hi(update, context):
    chat = update.effective_chat
    chat_id = chat.id
    message = update.message.text
    with open("post1.txt", 'r', encoding='utf-8') as file:
        text1 = file.read()
    if message == '1':
       context.bot.send_photo(chat_id, open('1.jpeg', 'rb'))
    elif message == '2':
        context.bot.send_photo(chat_id, open('2.jpeg', 'rb'))
    elif message == 'что такое GPT?':
        context.bot.send_audio(chat_id, open('gpt.mp3', 'rb'))
    elif message == 'в чем разница между SQL и NoSQL?':
        context.bot.send_audio(chat_id, open('nosql.mp3', 'rb'))
    elif message == 'история первой любви':
        context.bot.send_audio(chat_id, open('love.mp3', 'rb'))
    elif (message == 'пост') or (message == 'Пост'):
        context.bot.send_message(chat_id, text1)
    elif (message == 'код') or (message =='Код'):
        context.bot.send_message(chat_id, 'https://github.com/Goryunova/yander_bot')
    else:
        context.bot.send_message(chat_id, text='Привет, я Bot!')

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.last_name
    buttons = ReplyKeyboardMarkup([['1', '2'],
    ['что такое GPT?', 'в чем разница между SQL и NoSQL?', 'история первой любви']])
    context.bot.send_message(
        chat_id=chat.id,
        text='Спасибо, что вы включили меня, {}!'.format(name),
        reply_markup=buttons  
        )

updater.dispatcher.add_handler(CommandHandler('start', wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling()
updater.idle() 