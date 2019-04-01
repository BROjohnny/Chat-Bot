from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('hy master')
bot.set_trainer(ListTrainer)

for files in os.listdir('english'):
    data = open('english/' + files , 'r').readlines()
    #data.readlines()
    bot.train(data)

while True:
    message = input('you :')
    if message.strip() != 'bye':
        reply = bot.get_response(message)
        print('master :' + str(reply))

    if message.strip() == 'bye':
        print("master : bye")
        break