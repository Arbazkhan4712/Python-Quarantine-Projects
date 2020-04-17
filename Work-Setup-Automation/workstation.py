import os 
import webbrowser as wb

def workstation():
	codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"#ADD THE PATH OF TXET EDITOR OR IDE HERE
	os.startfile(codePath)
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'#ADD THE PATH OF CHROME HERE
	URLS = (
	        "stackoverflow.com", 
	        "github.com/Arbazkhan4712", 
	        "gmail.com",
	        "google.com",
	        "youtube.com"
	        )#ADD THE WEBSITES YOU USE WHIE WORKING
	for url in URLS:
		wb.get(chrome_path).open(url)
workstation()
