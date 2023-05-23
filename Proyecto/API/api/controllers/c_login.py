from flask import jsonify, request
from models.user import *

m_user= user()
class c_login():
  
    def s_login(self):
        query=m_user.login()
        return query