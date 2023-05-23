from flask import jsonify, request
from models.m_chart import *

mod_charts= chart()

class chartcontroller():
    def c_consultar_jobs(self):
        query=mod_charts.m_get_jobs()
        return query
    