import ephem_bot_settings, logging, ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename='TEST.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s [%(levelname)s]: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def greet_user(update, context):
    update.message.reply_text('Вызвана команда /start')


def know_constellation (update, context):
    object_input = update.message.text.split()[1].lower()
    today = datetime.now()
    objects = {
        'солнце': ephem.Sun,
        'луна': ephem.Moon,
        'меркурий': ephem.Mercury,
        'венера': ephem.Venus,
        'марс': ephem.Mars,
        'юпитер': ephem.Jupiter,
        'сатурн': ephem.Saturn,
        'уран': ephem.Uranus,
        'нептун': ephem.Neptune,
        'плутон': ephem.Pluto,
    }
    if object_input in objects:
        object_in = ephem.constellation(objects[object_input](today))
        update.message.reply_text(object_in[1])
    elif object_input == 'земля':
        update.message.reply_text('Невозможно определить в каком созвездии находится Земля, т.к. мы наблюдаем с неё :)')
    else:
        update.message.reply_text('Извините, данные введены некорректно, или такого небесного тела нет в базе данных :(')


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)


def main():
    mybot = Updater(ephem_bot_settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', know_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('BOT STARTED')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
