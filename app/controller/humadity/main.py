from flask import request, jsonify
from flask_restful import Resource
from app.controller.mqtt.main import sensor_data

class Temperature(Resource):
    def get(self):
        return jsonify({"temperature": sensor_data["temperature"]})
    
class Humadity(Resource):
    def get(self):
        return jsonify({"humidity": sensor_data["humidity"]})
    
class Sensor(Resource):

    def get(self):
        return jsonify(sensor_data)