from flask import Flask, render_template
from sense_hat import SenseHat 

app = Flask(__name__)

@app.route('/') 

def index():

	sense = SenseHat() 
	
	celcius = round(sense.get_temperature(), 2) 
	fahrenheit = round(1.8 * celcius + 32, 2)
	humidity = round(sense.get_humidity(), 2)
	pressure = round(sense.get_pressure(), 2)
	
	
	X = [255,0,0]
	O = [255,255,255]
	
	question_mark = [
	O, O, O, X, X, O, O, O,
	O, O, X, O, O, X, O, O,
	O, O, O, O, O, X, O, O,
	O, O, O, O, X, O, O, O,
	O, O, O, X, O, O, O, O,
	O, O, O, X, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, X, O, O, O, O
]
	sense.set_pixels(question_mark)
	
	
	
	return render_template('dashboard.html', celcius = celcius, fahrenheit = fahrenheit, 
	humidity = humidity, pressure = pressure)
	
if __name__ == '__main__': 
	app.run(debug=True, host='0.0.0.0')
