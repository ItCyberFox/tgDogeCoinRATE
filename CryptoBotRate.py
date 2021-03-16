import requests
from datetime import datetime
import telebot
from auth_data import token
import traceback


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


bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"Hello friend! Write the '/doge, /btc or /eth' to find out the cost of DOGE BTC OR ETH!")



@bot.message_handler(commands=["doge"])
def senddoge_text(message):
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
def sendbtc_text(message):
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
def sendeth_text(message):
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



if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        pass
