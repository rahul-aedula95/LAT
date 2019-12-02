from flask import Flask, request, Response
import jsonpickle
import io
import hashlib
import pika
import base64
import pickle

import socket
import mysql.connector


# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/success/', methods=['GET'])
def suc():
    dbIp="35.247.114.246"
    dbIp="localhost"
    mydb = mysql.connector.connect(host=dbIp,database='successMetrics',user='TESTUSER',password='Pass_123',port=3306)

    mycursor = mydb.cursor()

    sql = "SELECT COUNT(*) FROM status;"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()[0]
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    message={'count of successes':myresult[0]}
    # convert the data to a PIL image type so we can extract dimensions
    try:

        response = message
    except:
        response = { 'count' : 0}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/failure/', methods=['GET'])
def fail():
    dbIp="35.247.114.246"
    dbIp="localhost"
    mydb = mysql.connector.connect(host=dbIp,database='failureMetrics',user='TESTUSER',password='Pass_123',port=3306)

    mycursor = mydb.cursor()

    sql = "SELECT COUNT(*) FROM failure;"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()[0]
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    message={'count of failures':myresult[0]}
    # convert the data to a PIL image type so we can extract dimensions
    try:

        response = message
    except:
        response = { 'count' : 0}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")




# start flask app
app.run(host="0.0.0.0", port=5000)
