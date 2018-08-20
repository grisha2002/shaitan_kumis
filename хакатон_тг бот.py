import telebot
import serial  
alarm_clock = False
door = False
light = False

rdy = False
while not rdy:
    try:
        ser = serial.Serial('COM3', 9600)
        rdy = True
    except:
        print("Could not open")
        

token = "698691678:AAGn_6fFvsSnjvcjOXMAlHovfiIQkcNs-Qw"
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    user_id = message.chat.id
    bot.send_message(user_id, "привет,для управления дверью напишите команду /door_open(открыть дверь) или /door_close(закрыть дверь)")
    bot.send_message(user_id, "для управления светом напишите команду /light_on(открыть дверь) или /light_off(выключить свет)")
    bot.send_message(user_id, "для управления будильником напишите команду /alarm_clock_on(включить будильник) или /alarm_clock_off(выключить будильник)")
    
@bot.message_handler(commands=['door_open'])    
def door_open(message):
    global ser
    user_id = message.chat.id
    bot.send_message(user_id,"дверь открыта")
    door = True
    print('door_open')
    try:
        ser.write(b'3')
    except:
        print('write_error')

@bot.message_handler(commands=['door_close'])    
def door_close(message):
    global ser
    user_id = message.chat.id
    bot.send_message(user_id,"дверь закрыта")
    door = False
    print('door_close')
    try:
        ser.write(b'4')
    except:
        print('write_error')
    
@bot.message_handler(commands=['light_on'])    
def light_on(message):
    global ser
    user_id = message.chat.id
    bot.send_message(user_id,"свет включен")
    light = True
    print('light_on')
    try:
        ser.write(b'1')
    except:
        print('write_error')
    
    
@bot.message_handler(commands=['light_off'])    
def light_off(message):
    user_id = message.chat.id
    bot.send_message(user_id,"свет выключен")
    light = False
    print('light_off')
    try:
        ser.write(b'2')
    except:
        print('write_error')
@bot.message_handler(commands=['alarm_clock_on'])    
def door_on(message):
    global ser
    user_id = message.chat.id
    bot.send_message(user_id,"будильник включен")
    door = True
    print('alarm_clock_on')
    try:
        ser.write(b'5')
    except:
        print('write_error')
@bot.message_handler(commands=['alarm_clock_off'])    
def door_close(message):
    global ser
    user_id = message.chat.id
    bot.send_message(user_id,"будильник выключен")
    door = False
    print('alarm_clock_off')
    try:
        ser.write(b'6')
    except:
        print('write_error')
    
    
bot.polling(none_stop=True)



