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
    dbIp="10.138.15.211"
    #dbIp="localhost"
    mydb = mysql.connector.connect(host=dbIp,database='finishMetrics',user='restproject',password='Pass_123',port=3306)

    mycursor = mydb.cursor()

    sql = "SELECT COUNT(*) FROM finish;"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()[0]

    mydb.commit()
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
    dbIp="10.138.15.211"
    #dbIp="localhost"
    out = 0
    mydb = mysql.connector.connect(host=dbIp,database='finishMetrics',user='restproject',password='Pass_123',port=3306)

    mycursor = mydb.cursor()

    sql = "SELECT COUNT(*) FROM finish;"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()[0]
    out -= int(myresult[0])
    mydb.commit()


    mydb = mysql.connector.connect(host=dbIp,database='startMetrics',user='restproject',password='Pass_123',port=3306)

    mycursor = mydb.cursor()

    sql = "SELECT COUNT(*) FROM start;"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()[0]
    out += int(myresult[0])
    mydb.commit()

    message={'count of failures':str(out)}
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
