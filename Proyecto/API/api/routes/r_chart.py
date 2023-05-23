from flask import Flask, jsonify, request, Blueprint
from flask_cors import  cross_origin
from controllers.c_chart import *

chart = Blueprint('chart', __name__)

con_chart = chartcontroller()

@chart.route('/jobs', methods=['GET'])
@cross_origin()
def jobs():
  return  con_chart.c_consultar_jobs()
