# app.py
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/temperature', methods=['GET'])
def get_temperature():
    location = request.args.get('location')
    sensor_id = request.args.get('sensorId')

    # логика из задания
    if not location:
        if sensor_id == '1':
            location = 'Living Room'
        elif sensor_id == '2':
            location = 'Bedroom'
        elif sensor_id == '3':
            location = 'Kitchen'
        else:
            location = 'Unknown'
    if not sensor_id:
        if location == 'Living Room':
            sensor_id = '1'
        elif location == 'Bedroom':
            sensor_id = '2'
        elif location == 'Kitchen':
            sensor_id = '3'
        else:
            sensor_id = '0'

    temp = round(random.uniform(-10, 40), 1)
    return jsonify({
        "sensorId": sensor_id,
        "location": location,
        "temperature": temp,
        "unit": "celsius"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)