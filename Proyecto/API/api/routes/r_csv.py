from flask import Flask, jsonify, request, Blueprint
from flask_cors import  cross_origin
from controllers.c_csv import *

con_csv= csvcontrolador()

csv = Blueprint('csv', __name__)

@csv.route('/getcsv', methods=['GET'])
@cross_origin()
def listacsv():
  return con_csv.c_consultar_csv()