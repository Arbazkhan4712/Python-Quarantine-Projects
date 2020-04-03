import telepot, time, serial
from serial import Serial
ser = serial.Serial('com3', 9600)

def bot(msg):

	userName = msg['from']['first_name']+" "+msg['from']['last_name']

	content_type, chat_type, chat_id = telepot.glance(msg)

	if (content_type == 'text'):
		command = msg['text']
		print ('Got command: %s' % command)

		if  'hello' in command:
			bot.sendMessage(chat_id, "Hello, This is robotic chatbot created by ARBAZ KHAN. You can use this bot for home automation. Nice to chat with you.):")

		if 'on' in command:
			ser.write(b'Y')
			bot.sendMessage(chat_id, "Lamp ON")

		if 'off' in command:
			ser.write(b'N')
			bot.sendMessage(chat_id, "Lamp OFF")


bot = telepot.Bot('')# add your api key
bot.message_loop(bot)


while 1:
	time.sleep(20)
