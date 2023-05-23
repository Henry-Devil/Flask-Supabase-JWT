#from config import *
#from flask import jsonify, 

from flask import request, jsonify
from flask_jwt_extended import create_access_token
import supabase

class user():

    def login(self):
        username = request.json.get('username')
        password = request.json.get('password')

        SUPABASE_URL = 'https://tvelvelhkaauhahaqudb.supabase.co'
        SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR2ZWx2ZWxoa2FhdWhhaGFxdWRiIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODMxMjkzMjgsImV4cCI6MTk5ODcwNTMyOH0.ee4dFgjFtNIkxTtZddY6MJ_6oyp0D7ije6daRuyneaU'
        # Conectamos con Supabase
        client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

        # Buscamos el usuario en la tabla 'users'
        query = client.table('users').select('*').eq('username', username).eq('password', password)
        res = query.execute()
         #Si el usuario existe y la contraseña es correcta, se devuelve un token JWT
        if len(res.data) == 1:
            access_token = create_access_token(identity=username)
            print("access_token generado con éxito")

        return jsonify({"acceso": "AUTORIZADO", "access_token": access_token})

