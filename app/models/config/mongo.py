from pymongo.mongo_client import MongoClient

class MongoDB:

    def __init__(self):
        self.__uriMongo = "mongodb+srv://rqwannn:9v6ipIeM8gPHleqm@sic.ywzn2iw.mongodb.net/?retryWrites=true&w=majority&appName=SIC"
        self._client =  MongoClient(self.__uriMongo)
        self._database = self._client["SIC"]

    def getURL(self):
        return self.__uriMongo
    
    def check_connection(self):
        try:
            self._client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)