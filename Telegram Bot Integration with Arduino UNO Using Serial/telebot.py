import telepot, time, serial
from serial import Serial
ser = serial.Serial('com3', 9600)

def sreebot(msg):

	userName = msg['from']['first_name']+" "+msg['from']['last_name']

	content_type, chat_type, chat_id = telepot.glance(msg)

	if (content_type == 'text'):
		command = msg['text']
		print ('Got command: %s' % command)

		if  'hello' in command:
			bot.sendMessage(chat_id, "Hello , Hello, This is robotic chatbot created by Shreekant Gosavi. You can use this bot for home automation. Nice to chat with you.):")

		if 'on' in command:
			ser.write(b'Y')
			bot.sendMessage(chat_id, "Lamp ON")

		if 'off' in command:
			ser.write(b'N')
			bot.sendMessage(chat_id, "Lamp OFF")


bot = telepot.Bot('971334691:AAH4vXJSGjbA7d_YkB6mx8CQvzGwvEc421c')
bot.message_loop(sreebot)


while 1:
	time.sleep(20)