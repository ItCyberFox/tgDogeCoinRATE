import traceback
from datetime import datetime

import requests
import telebot
from telebot import types

from auth_data import token


def get_rub():
    req = requests.get("https://yobit.net/api/3/ticker/usd_rur")
    response = req.json()
    sell_price = response["usd_rur"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell DOGE price: {sell_price}")


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
    chat_id = message.chat.id
    print(chat_id)

    print(message.text)

    try:

        bot.send_message(message.chat.id,
                         "Этот самурай пока мало что может, но я работаю над его функционалом. Напиши /ls")


    except Exception as e:
        pass


@bot.message_handler(commands=["ls"])
def main_message(message):
    bot.send_message(message.chat.id,
                     "/rate-курсы крипты🔣\n/help - помощь🗿\n/file - файлохранилище📦\n /pay - Оплатить скрипт")


@bot.message_handler(commands=["pay"])
def pay_qiwi(message):
    bot.send_message(message.chat.id,
                     "🛠|Оплатить скрипт:  \n📲|https://qiwi.com/p/79167537704\n💳|price:30$\n📨|оставьте свой тг в "
                     "коментариях к платежу")


@bot.message_handler(commands=["file"])
def file(message):
    bot.send_message(message.chat.id, "💾отправь файл💾\n📫я пришлю тебе ключ📫\n📭отправь мне его, и получишь свой файл📭")


@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id, "Для получения помощи напишите @Code_Samurai")


# -----------------------выводит на выбор 3 монеты для получения информации об их курсе---------------------------------


@bot.message_handler(commands=["rate"])
def start_message(message):
    bot.send_message(message.chat.id, "/doge - |DogeCoin \n/btc -  |BitCoin \n/eth - |Ethereum\n/rub - |Ruble")


# ----------------------команды для вывода курса монет------------------------------------------------------------------
@bot.message_handler(commands=["doge"])
def doge_text(message):
    try:
        req = requests.get("https://yobit.net/api/3/ticker/doge_usd")
        response = req.json()
        sell_price = response["doge_usd"]["sell"]
        bot.send_message(
            message.chat.id, f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n 🧡𝐒𝐞𝐥𝐥 𝐃𝐎𝐆𝐄 𝐩𝐫𝐢𝐜𝐞: {sell_price}\n "
                            f"🧡𝐃𝐨𝐠𝐞𝐏𝐨𝐰𝐞𝐫[.]({img})", parse_mode='markdown'

                             
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


@bot.message_handler(commands=["rub"])
def rub_text(message):
    try:
        req = requests.get("https://yobit.net/api/3/ticker/usd_rur")
        response = req.json()
        sell_price = response["usd_rur"]["sell"]
        bot.send_message(
            message.chat.id,
            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell RUB price: {sell_price}"
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

# бот принимает file_id и отправляет файл привязанный к нему
@bot.message_handler(content_types=["text"])
def send_file(message):
    try:
        ss = message.text
        bot.send_document(message.chat.id, ss)



    except:
        ...


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        ...

