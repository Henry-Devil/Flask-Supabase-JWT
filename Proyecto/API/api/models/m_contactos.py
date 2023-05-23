from config import *
from flask import jsonify, request


class Contactos():
    
    def getDatos(self):
        return {
            'id': self.id,
            'correo': self.correo,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono
            }

    def m_consultar_contactos(self):
        try:
            cursor = connection.cursor()
            cursor.execute("select id, correo, nombre, apellido, telefono from contactos ;")
            rv = cursor.fetchall()
            cursor.close()
           
            payload = []
            content = {}
            for result in rv:
                content = {'id': result[0],
                           'correo': result[1],
                           'nombre': result[2],
                           'apellido': result[3],
                           'telefono': result[4]}
                
                payload.append(content)
                content = {}
            #print(payload)
            return jsonify(payload)
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({"informacion":error})
        finally:
            pass
        
    def m_crear_contactos(self):
        try:           
            correo = request.json['correo'] 
            nombre = request.json['nombre']       
            apellido = request.json['apellido']     
            telefono = request.json['telefono'] 
              
            cursor = connection.cursor()
            codi="INSERT INTO contactos (correo, nombre, apellido, telefono) VALUES (%s, %s, %s, %s)"
            vari=(correo, nombre, apellido, telefono)
            cursor.execute(codi,vari,)
            cursor.connection.commit()
            cursor.close()
            
            return jsonify({"informacion":"ok"})
            
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({"informacion":error})
        finally:
            pass
    
    def m_consultar_contactos_id(self):
        try:
            id = request.json['id'] 
          
            cursor = connection.cursor()
            cursor.execute("SELECT * from contactos WHERE id=(%s);", (id,))
            rv = cursor.fetchall()
            cursor.close()
            print(record)
            payload = []
            content = {}
            for result in rv:
                content = {'id': result[0], 'correo': result[1], 'nombre': result[2], 'apellido': result[3], 'telefono': result[4]}
                payload.append(content)
                content = {}
            print(payload)
            return jsonify(payload)
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({"informacion":error})
        finally:
            pass

    def m_actualizar_contactos(self):
        try:           
            id = request.json['id'] 
            correo = request.json['correo']       
            nombre = request.json['nombre']     
            apellido = request.json['apellido'] 
            telefono = request.json['telefono'] 

            cursor = connection.cursor()
            codi="UPDATE contactos SET correo=%s, nombre=%s, apellido=%s, telefono=%s WHERE id=%s"
            vari=(correo, nombre, apellido, telefono,id)
            cursor.execute(codi,vari)
            cursor.connection.commit()
            cursor.close()
            
            return jsonify({"informacion":"ok"})
            
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({"informacion":error})
        finally:
            pass

    def m_bajar_contacto(self):

        try:           
            id = request.json['id'] 
            cursor = connection.cursor()
            codi="DELETE FROM contactos WHERE id=%s"
            vari=(id,)
            cursor.execute(codi, vari)
            cursor.connection.commit()
            cursor.close()
            
            return jsonify({"informacion":"ok"})
            
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({"informacion":error})
        finally:
            pass


        