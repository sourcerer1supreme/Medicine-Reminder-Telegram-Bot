from datetime import *
from pytz import *
from telegram import *
from telegram.ext import *
import time

medicine_timings = {
    "06:00" : "Detox Water.",
    "08:00" : "Homeo 1.",
    "09:15" : "Eyedrop 1.",
    "09:30" : "Vitamins after breakfast.",
    "12:00" : "Homeo 2.",
    "19:30" : "Homeo 3.",
    "21:15" : "Eyedrop 2",
    "23:26" : "test-med1",
    "23:27" : "test-med2",
}

current_time = datetime.now(timezone('Asia/Kolkata'))
current_time_string = current_time.strftime("%H:%M")

print("time: ", current_time_string)


API_Key = "*******************************" #key here
CHAT_ID = "****************" #chat ID here

bot = Bot(API_Key)
updater = Updater(API_Key, use_context=True)
updater.start_polling() 

while(True):

    current_time = datetime.now(timezone('Asia/Kolkata'))
    current_time_string = current_time.strftime("%H:%M")

    if current_time_string in medicine_timings:
        message = "Medicine Reminder: "+medicine_timings[current_time_string]
        print(message)
        bot.send_message(
            chat_id = CHAT_ID,
            text = message
        )
        time.sleep(61)

    time.sleep(1)


updater.stop()
