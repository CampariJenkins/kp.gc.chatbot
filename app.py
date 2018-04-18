from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from pymongo import MongoClient
import os
import ssl

app = Flask(__name__)

#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

import logging
logging.basicConfig(level=logging.DEBUG)

print ("start")

#client = MongoClient("mongodb://kp-devops:TlZmBPJBNrSCWkawD31t5IbR9pyfiIxufiINEVkAHijEtJ8NwT6ZfofqQUYP1NrQK0ZEFS8zPysIOr0u1p2xwA==@kp-devops.documents.azure.com:10255/?ssl=true&replicaSet=globaldb",ssl_cert_reqs=ssl.CERT_NONE) #host uri
#db = client.mongoChat    #Select the database
#db.authenticate(name="kp-devops",password='TlZmBPJBNrSCWkawD31t5IbR9pyfiIxufiINEVkAHijEtJ8NwT6ZfofqQUYP1NrQK0ZEFS8zPysIOr0u1p2xwA==')

print ("conn che non serve creata")

## Comment out when running locally
#client = MongoClient(os.getenv("MONGOURL"))
#db = client.test    #Select the database
#db.authenticate(name=os.getenv("MONGO_USERNAME"),password=os.getenv("MONGO_PASSWORD"))
#todos = db.todo #Select the collection

#english_bot = ChatBot(
    #'Mongoloide',
    #storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    #database='mongoChat',
    #database_uri='mongodb://172.17.0.2:27017/',
    #database_uri='mongodb://kp-devops:TlZmBPJBNrSCWkawD31t5IbR9pyfiIxufiINEVkAHijEtJ8NwT6ZfofqQUYP1NrQK0ZEFS8zPysIOr0u1p2xwA==@kp-devops.documents.azure.com:10255/?ssl=true&replicaSet=globaldb',
    #database_uri='mongodb://kp-devops:TlZmBPJBNrSCWkawD31t5IbR9pyfiIxufiINEVkAHijEtJ8NwT6ZfofqQUYP1NrQK0ZEFS8zPysIOr0u1p2xwA==@kp-devops.documents.azure.com:10255/?ssl=true&replicaSet=globaldb&ssl_ca_certs=/Users/rocco/Downloads/TLSCA5.pem',
    #database_uri=os.getenv("MONGOLOIDE")
    #trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    #trainer='chatterbot.trainers.ListTrainer'
#)

#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

#@app.route("/get")
#def get_bot_response():
#    userText = request.args.get('msg')
#    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5555)
    app.run()
