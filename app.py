from flask import Flask, jsonify, render_template
import time

from sensor import read_temperature

app = Flask(__name__)

temp_data = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    global temp_data
    temp_data.append({'time': time.strftime('%H:%M:%S'), 'temperature': read_temperature()})
    if len(temp_data) > 20:
        temp_data.pop(0)
    return jsonify(temp_data)


if __name__ == '__main__':
    app.run(debug=True)
