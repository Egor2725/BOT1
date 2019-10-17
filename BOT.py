import requests
from bot_config import token
from bot_config import time
from time import sleep
global last_upd, money_list

last_upd = 0
money_list = {}
class Bot:

    def __init__(self,token):
        self.token = token  
        self.url = f'https://api.telegram.org/bot{self.token}/'

    def get_updates(self):
        method = 'getUpdates'
        req = requests.get(self.url + method)
        if req.status_code in list(range(200, 300)):                  #2хх         #Обработка статуса запроса
            print("Успех. Response "+str(req.status_code))
        elif req.status_code in list(range(300, 400)):                #3xx
            print("Перенаправление. Response "+str(req.status_code))
        elif req.status_code in list(range(400, 500)):                #4xx
            print("Ошибка клиента. Response "+ str(req.status_code))
        elif req.status_code in list(range(500, 600)):                #5xx
            print("Ошибка сервера. Response "+ str(req.status_code))


        return req.json()

    def get_message(self):
        data = self.get_updates()
        
        last_obj = data['result'][-1]
        curr_update_id = last_obj['update_id']

        global last_upd, last_message
        if last_upd != curr_update_id:
            last_upd = curr_update_id
            last_message = data['result'][-1]['message']
            chat_id = last_message['chat']['id']
            text = last_message['text']
            message = {
                    'chat_id': chat_id,
                    'text': text,
                }
            return message
        return None

        
        


    def send_message(self, chat_id, text):
        method = 'sendMessage'
        response = requests.post(self.url + method+'?chat_id={}&text={}'.format(chat_id, text))
        return response

class MoneyBot(Bot):

    def __init__(self, token):
        super().__init__( token)  
        self.money_url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
        
    def get_money(self):
        response = requests.get(self.money_url).json()
        # money_list={}
        # global money_list
        for item in list(response):
            money = {item['Cur_Abbreviation']: item['Cur_OfficialRate']}
            money_list.update(money)
            

        # return money_list   
        # return answer_money
        # print (money_list)   
        
    def find_money(self, answer_money):

        # value = money_list[answer_money]
        answer_money = ("'"+answer_money+"'")
        # print(answer_money)
        am=answer_money
        # answer_money = dict(answer_money)
        value = money_list[am]
        
        return value

        


    # def record_message_to_file(self):                     #пока не сделано
    #     with open('/messages/message'+ ''.join(str(time).split(' '))+'.txt', 'w') as message_file:
    #         last_user_message = self.get_updates()['result'][-2]['message']['text']
    #         message_file.write(last_user_message+'/n')





