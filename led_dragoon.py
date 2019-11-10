from flask import Flask, render_template
from flask_mqtt import Mqtt

app = Flask(__name__)
app.config['MQTT_BROKER_PORT'] = 1883
mqtt = Mqtt(app)
print("Halloooooo")


def mqtt_send(payload):
	mqtt.publish("/home/esp1/set", payload)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/funktion1')
def funktion1():
	mqtt_send('{"effect": "St Patty", "state": "ON"}')
	return render_template('index.html')

@app.route('/funktion2')
def funktion2():
	mqtt_send('{"effect": "USA", "state": "ON"}')
	return render_template('index.html')

@app.route('/funktion3')
def Funktion3():
	mqtt_send('{"effect": "Go Lions", "state": "ON"}')
	return render_template('index.html')

@app.route('/funktion4')
def funktion4():
	mqtt_send('{"effect": "Hue Breathe", "state": "ON"}')
	return render_template('index.html')

@app.route('/funktion5')
def funktion5():
	mqtt_send('{"effect": "Full Hue", "state": "ON"}')
	return render_template('index.html')

@app.route('/funktion6')
def funktion6():
	mqtt_send('{"effect": "rainbow", "state": "ON"}')
	return render_template('index.html')
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080, debug=True)
