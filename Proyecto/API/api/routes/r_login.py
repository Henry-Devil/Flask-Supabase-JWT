from flask import Flask, jsonify, request, Blueprint
from flask_cors import  cross_origin
from controllers.c_login import *


p_login = Blueprint('p_login', __name__)
con_inicio_sesion= c_login()


@p_login.route('/login', methods=['POST'])
@cross_origin()  
def login():
   return con_inicio_sesion.s_login()

