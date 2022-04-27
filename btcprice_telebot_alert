import time

import requests
#xpath="#xpath=//div[@jsname="ip75Cb"]"
#selector="body > c-wiz.zQTmif.SSPGKf.u5wqUe:nth-child(5) > div.T4LgNb:nth-child(1) > div.e1AOyf:nth-child(4) > div > div > main > div.Gfxi4:nth-child(2) > div.yWOrNb:nth-child(1) > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.QZMA8b:nth-child(1) > c-wiz:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div > div.rPF6Lc:nth-child(1) > div.ln0Gqe > div:nth-child(1) > div.AHmHk > span > div.kf1m0 > div.YMlKec.fxKbKc"
from lxml import html
import random
from bs4 import BeautifulSoup
import telebot

def get_btc_price():
    try:
        URL_ADDRESS = 'https://www.google.com/finance/quote/BTC-USD'
        USER_AGENTS = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
        ]
        header = {
            'User-Agent': random.choice(USER_AGENTS),
        }
        req_content = requests.get(URL_ADDRESS, headers=header).text
        soup = BeautifulSoup(req_content)
        results = soup.select('div.kf1m0')
        datas = []
        for data in results:
            try:
                result = data.getText()
                btc_price = result.replace(",", "").split('.')[0]
            except:
                btc_price = ''
            datas.append(btc_price)
    except Exception as E:
        print('解析错误:{}'.format(E))
    return datas[0]

from datetime import datetime

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello, friend! Write 'price' to find the cost of BTC! and Alert beging started")
        while True:
            try:
                #
                send_times=3
                current_price=int(get_btc_price())
                print("BTC CURRENT PRICE:{}".format(current_price))
                if current_price >=41000:
                    while current_price >=41000:
                        while send_times>0:
                            bot.send_message(message.chat.id, "BTC!!! PRICE IS:{} U HAVE TO SELL SOME LIKE %30".format(current_price))
                            send_times-=1
                            current_price = int(get_btc_price())
                            time.sleep(30)
                elif current_price>=42000:
                    while current_price >=42000:
                        while send_times > 0:
                            bot.send_message(message.chat.id, "BTC!!! PRICE IS:{} U HAVE TO SELL SOME LIKE %40".format(current_price))
                            send_times-=1
                            current_price = int(get_btc_price())
                            time.sleep(30)
                elif current_price<=38000:
                    while current_price <= 38000:
                        while send_times > 0:
                            bot.send_message(message.chat.id,"!!! NOW BTC PRICE IS:{} U HVAE TO BUY ARROUND 25% ".format(current_price))
                            send_times -= 1
                            current_price = int(get_btc_price())
                            time.sleep(30)
                elif current_price<=35000:
                    while current_price <=35000:
                        while send_times > 0:
                            bot.send_message(message.chat.id,"!!! NOW BTC PRICE IS:{} U HVAE TO BUY ARROUND 50% ".format(current_price))
                            send_times -= 1
                            current_price = int(get_btc_price())
                            time.sleep(30)

            except Exception as E:
                bot.send_message(message.chat.id, "Oops... Something was wrong!!!{}".format(E))
            time.sleep(30)

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text == "price":
            try:
                sell_price=get_btc_price()
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nBTC price: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Oops... Something was wrong!!!"
                )
        else:
            bot.send_message(message.chat.id, "Wrong! Check your command please!")

    bot.polling()

if __name__ == "__main__":
    tgbot_token=""
    telegram_bot(tgbot_token)
