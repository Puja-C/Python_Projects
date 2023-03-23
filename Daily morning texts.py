import schedule
import time
import requests
from Credentials import Phone_number


def send_message() :
    resp = requests.post('https://textbelt.com/text', {
        'phone': Phone_number,
        'message': 'Hey, Good Morning!',
        'key': 'textbelt',        # textbelt --> allows one msg a day
    })

    print(resp.json())


schedule.every().day.at('06:00').do(send_message())

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
