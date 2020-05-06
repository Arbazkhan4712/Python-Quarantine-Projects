from flask import Flask, render_template, request, redirect
from gpiozero import LED
from time import sleep
led = LED(2)

app = Flask(__name__)

@app.route("/")

def home():
    if led.value == 1:
        status = 'ON'
    else:
        status = 'OFF'
    return render_template('home.html', status=status)


@app.route("/on")

def on():
    led.on()
    return "LED on"

@app.route("/off")

def off():
    led.off()
    return "LED off"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000) 

