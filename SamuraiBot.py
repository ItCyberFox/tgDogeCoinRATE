import requests
from datetime import datetime
import telebot
from auth_data import token
import traceback


# ----------------------тут запросы к API бирже и узнает курс криптовалют-----------------------------------------------


def get_doge():
    req = requests.get("https://yobit.net/api/3/ticker/doge_usd")
    response = req.json()
    sell_price = response["doge_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell DOGE price: {sell_price}")


def get_btc():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")


def get_eth():
    req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
    response = req.json()
    sell_price = response["eth_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell ETH price: {sell_price}")





# ---------------------------тут стартовые команды для общения с ботом--------------------------------------------------


bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Этот самурай пока мало что может, но я работаю над его функционалом. Напиши /ls")


@bot.message_handler(commands=["ls"])
def main_message(message):
    bot.send_message(message.chat.id, "/rate-курсы крипты🔣\n/help - помощь🗿\n/file - файлохранилище📦")


@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id, "Для получения помощи напишите @Code_Samurai")


# -----------------------выводит на выбор 3 монеты для получения информации об их курсе---------------------------------


@bot.message_handler(commands=["rate"])
def start_message(message):
    bot.send_message(message.chat.id, "/doge - |DogeCoin \n/btc -  |BitCoin \n/eth - |Ethereum")


# ----------------------команды для вывода курса монет------------------------------------------------------------------
@bot.message_handler(commands=["doge"])
def doge_text(message):
    try:
        req = requests.get("https://yobit.net/api/3/ticker/doge_usd")
        response = req.json()
        sell_price = response["doge_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell DOGE price: {sell_price}"
        )


    except Exception as e:
        traceback.print_exc(e)
        bot.send_message(
            message.chat.id,
            "Damn...Something was wrong..."
        )


@bot.message_handler(commands=["btc"])
def btc_text(message):
    try:
        req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
        response = req.json()
        sell_price = response["btc_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
        )


    except Exception as e:
        traceback.print_exc(e)
        bot.send_message(
            message.chat.id,
            "Damn...Something was wrong..."
        )


@bot.message_handler(commands=["eth"])
def eth_text(message):
    try:
        req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
        response = req.json()
        sell_price = response["eth_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell ETH price: {sell_price}"
        )

    except Exception as e:
        traceback.print_exc(e)
        bot.send_message(
            message.chat.id,
            "Damn...Something was wrong..."
        )


# --------------------------------------------------тут все что связанно с отправкой фото и файлами---------------------


# @bot.message_handler(commands=["photo"])
# def photo(message):
#   """
#
#   :type message: photo
#  """
# with open(r"C:\Users\te1ho\Desktop\tmp\1234.jpg", "rb") as photo:
#    bot.send_photo(message.chat.id, photo)
# ----------------------------ниже бот сохраняет по указаному пути файлы которые ему отправят---------------------------



@bot.message_handler(content_types=["document", "video", "audio"])
def handle_files(message):
    try:
        document_id = message.document.file_id
        file_info = bot.get_file(document_id)

        print(document_id)  # Выводим file_id
        print(f'http://api.telegram.org/file/bot{token}/{file_info.file_path}')  # Выводим ссылку на файл

        bot.send_message(message.chat.id, document_id)  # Отправляем пользователю file_id


    except:
        ...





if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        ...
