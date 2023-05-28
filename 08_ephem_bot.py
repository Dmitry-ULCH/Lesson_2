import logging, ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename='TEST.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s [%(levelname)s]: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def greet_user(update, context):
    start = 'Вызвана команда /start'
    print(start)
    update.message.reply_text(start)


def know_constellation (update, context):
    planet_input = update.message.text
    today = datetime.now()
    planets = {'Sun': ephem.Sun,
               'Moon': ephem.Moon,
               'Mercury': ephem.Mercury,
               'Venus': ephem.Venus,
               'Mars': ephem.Mars,
               'Jupiter': ephem.Jupiter,
               'Saturn': ephem.Saturn,
               'Uranus': ephem.Uranus,
               'Neptune': ephem.Neptune,
               'Pluto': ephem.Pluto,
    }
    if planet_input in planets:
        planet_in = ephem.constellation(planets[planet_input](today))
        print(planet_in)
        update.message.reply_text(planet_in)
    else:
        update.message.reply_text('Извините, такой планеты нет в базе данных')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("5991348713:AAECDnmclQbKxnuhMSxW8PExo8MwkFmQq_s", use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', know_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('BOT STARTED')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

"""
Не выполняется команда /planet. Не могу никак понять, в чём ошибка.
Log выдаёт:

telegram.ext.dispatcher [ERROR]: No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "C:\Users\Dmitry\AppData\Local\Programs\Python\Python311\Lib\site-packages\telegram\ext\dispatcher.py", line 557, in process_update
    handler.handle_update(update, self, check, context)
  File "C:\Users\Dmitry\AppData\Local\Programs\Python\Python311\Lib\site-packages\telegram\ext\handler.py", line 199, in handle_update
    return self.callback(update, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "d:\_IT\GitHub\Learn_Python\Lesson_2\08_ephem_bot.py", line 19, in know_constellation
    planet_input = update.message.text
                   ^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'text'

"""