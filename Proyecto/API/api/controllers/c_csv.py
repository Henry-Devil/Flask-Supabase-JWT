from flask import jsonify, request
from models.m_csv import *

mod_csv= Csv()

class csvcontrolador():
    def c_consultar_csv(self):
        query=mod_csv.m_consultar_csv()
        return query