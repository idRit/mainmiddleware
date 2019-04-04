from pymongo import MongoClient
import bcrypt

class dbModel:
    
    def __init__(self):
        self.client = MongoClient("mongodb+srv://red:blxgre369@cluster0-oaiys.mongodb.net/test?retryWrites=true")
        self.cred_db = self.client.main
        self.mainCollection = self.cred_db.main  

    def insertOne(self, ad, creationTime, desc, location, s_id, response, address):
        details = {
            'ad' : ad,
            'creationTime' : creationTime,
            'desc' : desc,
            'location' : location,
            's_id' : s_id,
            'response' : response,
            'address' : address
        }
        self.mainCollection.insert(details)

    def getAll(self) :
        cursor = self.mainCollection.find({})
        return cursor

    def connected(self):
        print('connected')
