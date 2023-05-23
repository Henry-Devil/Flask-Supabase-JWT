from config import *
from flask import jsonify, request

class chart():

    def m_get_jobs(self):
        
        cursor = connection.cursor()
        cursor.execute("SELECT trabajo FROM data")
        jobs = cursor.fetchall()

        cursor.close()
        # Devolver los datos en formato JSON
        return jsonify(jobs)
  

