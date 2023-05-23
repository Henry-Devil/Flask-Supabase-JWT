from flask import Flask, jsonify, request, Blueprint
from flask_cors import  cross_origin
from controllers.c_contactos import *


con_contactos= contactoscontrolador()

contactos = Blueprint('contactos', __name__)

@contactos.route('/getcontactos', methods=['GET'])
@cross_origin()
def listacontactos():
  return con_contactos.c_consultar_contactos()

@contactos.route('/setcontactos', methods=['POST'])
@cross_origin()
def crearcontactos():
  return con_contactos.c_crear_contacto()

@contactos.route('/idcontactos', methods=['GET','POST'])
@cross_origin()
def consultarcontactos():
  return con_contactos.c_consultar_contacto_id()

@contactos.route('/actualizarcontactos', methods=['POST'])
@cross_origin()
def actualizarcontactos():
  return con_contactos.c_actualizar_contacto_id()

@contactos.route('/eliminarcontactos', methods=['POST'])
@cross_origin()
def eliminarcontactos():
  return con_contactos.c_bajar_contacto()

