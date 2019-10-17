from BOT import MoneyBot
from bot_config import token
from time import sleep
sleep(10)
global answer_money

test_bot = MoneyBot(token)


# answer = test_bot.get_message()


while True:
    answer = test_bot.get_message()
    if answer != None:
        chat_id = answer['chat_id']
        text = answer['text']
        if  '/course' in text:
            test_bot.send_message(chat_id, 'какая валюта интересует?')
            #нужно обновить ответ
            answer = test_bot.get_message()
    
            chat_id = answer['chat_id']
            text = answer['text']
                
                        
            answer_money=text
            test_bot.find_money(answer_money)
            money = test_bot.find_money(answer_money)
            test_bot.send_message(chat_id, money)

        else:
            test_bot.send_message(chat_id, 'что?')

    # answer = test_bot.get_message()
    # if answer != None:
    #     chat_id = answer['chat_id']
    #     text = answer['text']
    #         #    print(text)
                    
    #     answer_money=text
    #     test_bot.find_money(answer_money)
    #     money = test_bot.find_money(answer_money)
    #     test_bot.send_message(chat_id, money)    
        
        

    else:
        continue
        sleep(3)

# def find_money():
#         answer = test_bot.get_message()
#         if answer != None:
#             chat_id = answer['chat_id']
#             text = answer['text']
#             cours_item = text
            



input()
