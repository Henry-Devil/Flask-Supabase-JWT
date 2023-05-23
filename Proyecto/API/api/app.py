from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from functools import wraps
from config import *
from routes.r_consultas import contactos
from routes.r_csv import csv
from routes.r_chart import chart
from routes.r_login import p_login
from flask_jwt_extended import JWTManager

key='secret_key_parking'


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret' # Clave secreta para firmar los JWT
cors = CORS(app, resources={ r"/*": {"origins": "http://127.0.0.1:5000"}})

jwt = JWTManager(app)

app.register_blueprint(contactos)
app.register_blueprint(csv)
app.register_blueprint(chart)
app.register_blueprint(p_login)

@app.route('/')
@cross_origin()  
def index():
    return jsonify({'message': 'La API esta en funcionamiento'})

if __name__=="__main__":
    app.run(port=5000, debug=True)
