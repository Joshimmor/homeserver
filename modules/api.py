# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 


# Import Libraries 
from app import app
from flask import jsonify , request
from redis import Redis
from rq import Queue

connection = Redis()
q = Queue(connection)

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  return jsonify({"message":"Hello from Flask!"})

@app.route('/tank',methods=['GET'])
def get_tank():
    return jsonify({"tempature":90.5,"humidity":60})
@app.route('/tank', methods=['POST'])
def post_tank():
    temp = request.get_json()
    
    return temp
