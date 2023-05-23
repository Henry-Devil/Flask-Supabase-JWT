from config import *
from flask import jsonify, request

class Csv():

    def getCsv(self):
        return {
            'age': self.age,
            'pdays': self.pdays,
            'emp_var_rate': self.emp_var_rate,
            'cons_price_idx': self.cons_price_idx,
            'cons_conf_idx': self.cons_conf_idx,
            'euribor3m': self.euribor3m,
            'job': self.job,
            'marital': self.marital,
            'education': self.education,
            'default': self.default,
            'housing': self.housing,
            'loan': self.loan,
            'contact': self.contact,
            'month': self.month,
            'day_of_week': self.day_of_week,
            'duration': self.duration,
            'campaign': self.campaign,
            'previous': self.previous,
            'poutcome': self.poutcome,
            'nr_employed': self.nr_employed,
            'y': self.y
            }

    def m_consultar_csv(self):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT edad, trabajo, civil, educacion, credito, vivienda, prestamo, contacto, mes, ultimasemana, duracion, campa, numdiascontacto, anterior, resulmarkanterior, tasavariempleo, indpreconsumo, indconfconsumo, euribor3m, nempleados, suscrito FROM data")
            rv = cursor.fetchall()
            cursor.close()
            
            payload = []
            content = {}
            for result in rv:
                content = {'edad': result[0],
                           'trabajo': result[1],
                           'civil': result[2],
                           'educacion': result[3],
                           'credito': result[4],
                           'vivienda': result[5],
                           'prestamo': result[6],
                           'contacto': result[7],
                           'mes': result[8],
                           'ultimasemana': result[9],
                           'duracion': result[10],
                           'campa': result[11],
                           'numdiascontacto': result[12],
                           'anterior': result[13],
                           'resulmarkanterior': result[14],
                           'tasavariempleo': result[15],
                           'indpreconsumo': result[16],
                           'indconfconsumo': result[17],
                           'euribor3m': result[18],
                           'nempleados': result[19],
                           'suscrito': result[20]
                           }
                
                payload.append(content)
                content = {}
            print(payload)
            return jsonify(payload)
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({"informacion":error})
        finally:
            pass

def m_crear_csv(self):
        try:           
            correo = request.json['correo'] 
            nombre = request.json['nombre']       
            apellido = request.json['apellido']     
            telefono = request.json['telefono'] 
              
            cursor = connection.cursor()
            codi="INSERT INTO data (correo, nombre, apellido, telefono) VALUES (%s, %s, %s, %s)"
            vari=(correo, nombre, apellido, telefono)
            cursor.execute(codi,vari,)
            cursor.connection.commit()
            cursor.close()
            
            return jsonify({"informacion":"ok"})
            
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({"informacion":error})
        finally:
            pass
    
