import os
from pymongo import MongoClient

#Database setting

MONGO_URI = os.environ.get('MONGOHQ_URL') if os.environ.get('MONGOHQ_URL') is not None \
    else 'mongodb://adhelhgi:Cintamatiku20`@ds223343.mlab.com:23343/testlhgi'

client = MongoClient(MONGO_URI)
DB = client.get_default_database().name if client.get_default_database() is not None else 'task_database'
client.close()
