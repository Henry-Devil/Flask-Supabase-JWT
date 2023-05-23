from flask import jsonify, request
from models.m_contactos import *

mod_usuario= Contactos()

class contactoscontrolador():
    def c_consultar_contactos(self):
        query=mod_usuario.m_consultar_contactos()
        return query

    def c_crear_contacto(self):
        query=mod_usuario.m_crear_contactos()
        return query

    def c_consultar_contacto_id(self):
        query=mod_usuario.m_consultar_contactos_id()
        return query

    def c_actualizar_contacto_id(self):
        query=mod_usuario.m_actualizar_contactos()
        return query

    def c_bajar_contacto(self):
        query=mod_usuario.m_bajar_contacto()
        return query