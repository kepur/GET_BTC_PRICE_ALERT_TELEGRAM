import time
import requests
import random
from bs4 import BeautifulSoup
import telebot
'''
pip install -r requirement.txt
pip install pyTelegramBotAPI
pip install requests
pip install BeautifulSoup4

'''
file_not_exist = '''
#!!!!Please create config.ini file put current directory and config 
alert_config.ini does not exist
'''
example = '''[TELEGRAM]
telegram_token = 
chat_id = -1001799067710
'''
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
        soup = BeautifulSoup(req_content,"html.parser")
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

def telegram_bot(token,chat_id):
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=["help"])
    def help_message(message):
        bot.send_message(message.chat.id, "type /price GET BTC PRICE NOW!\n"
                                          "type /start MONITOR LOWER PRICE")

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(chat_id, "type /price' get of BTC now!\n"
                                          "Alert beging started")
        while True:
            try:
                sleptime=random.randint(30,90)
                #告警次数
                send_times=3
                current_price=int(get_btc_price())
                print("BTC CURRENT PRICE:{}".format(current_price))
                if current_price >=41000:
                    while current_price >=41000:
                        while send_times>0:
                            bot.send_message(chat_id, "BTC!!! PRICE IS:{} U HAVE TO SELL SOME LIKE %30".format(current_price))
                            send_times-=1
                            current_price = int(get_btc_price())
                            time.sleep(sleptime)
                elif current_price>=42000:
                    while current_price >=42000:
                        while send_times > 0:
                            bot.send_message(chat_id, "BTC!!! PRICE IS:{} U HAVE TO SELL SOME LIKE %40".format(current_price))
                            send_times-=1
                            current_price = int(get_btc_price())
                            time.sleep(sleptime)
                elif current_price<=38000:
                    while current_price <= 38000:
                        while send_times > 0:
                            bot.send_message(chat_id,"!!! NOW BTC PRICE IS:{} U HVAE TO BUY ARROUND 25% ".format(current_price))
                            send_times -= 1
                            current_price = int(get_btc_price())
                            time.sleep(sleptime)
                elif current_price<=35000:
                    while current_price <=35000:
                        while send_times > 0:
                            bot.send_message(chat_id,"!!! NOW BTC PRICE IS:{} U HVAE TO BUY ARROUND 50% ".format(current_price))
                            send_times -= 1
                            current_price = int(get_btc_price())
                            time.sleep(sleptime)

            except Exception as E:
                bot.send_message(chat_id, "Oops... Something was wrong!!!{}".format(E))
            time.sleep(sleptime)


    # @bot.message_handler(content_types=["text"])
    # def send_text(message):
    #     if message.text == "price":
    @bot.message_handler(commands=["price"])
    def get_price_message(message):
        try:
            sell_price = get_btc_price()
            bot.send_message(
                chat_id,
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nBTC price: {sell_price}"
            )
        except Exception as ex:
            print(ex)
            bot.send_message(
                chat_id,
                "Oops... Something was wrong!!!\n{}".format(ex)
            )
    bot.polling()


if __name__ == "__main__":

    from configparser import RawConfigParser
    import os
    try:
        #windows path
        current_config = r'{}'.format(str(os.getcwd() + "\\config.ini"))
        #linux path
        #current_config = r'{}'.format(str(os.getcwd() + "\/alert_config.ini"))
        current_path = r'{}'.format(str(os.getcwd()))
        try:
            if os.path.exists(current_config):
                configini = RawConfigParser()
                configini.read(current_config, encoding='utf8')
                TELEGRAM_TOKEN = configini.get('TELEGRAM', 'TELEGRAM_TOKEN')
                CHAT_ID = configini.get('TELEGRAM', 'CHAT_ID')
                telegram_bot(TELEGRAM_TOKEN,chat_id=CHAT_ID)
            else:
                with open(current_path + "/" + "error.log", mode='w+', encoding="utf8") as output_error:
                    output_error.write(file_not_exist)
                with open(current_path + "/" + "config.ini", mode='w+', encoding="utf8") as output_error:
                    output_error.write(example)
        except:
            pass
    except :
        pass
