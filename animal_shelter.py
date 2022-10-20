from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://localhost:47640')
        #self.client = MongoClient('mongodb://%s:%s@localhost:47640/authMechanism=DEFAULT&authSource=AAC' % ('aacuser', 'password'))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary 
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
    
    # read functions
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False} ) ## return a cursor which a pointer to a list of results ( documents)
        return cursor
    
    def read(self, data):
        if data is not None:
             return self.database.animals.find(data, {"_id":False}) ## returns one document
        else:
            return "Nothing to search, because data parameter is empty"
        
        #Update function
     
    def update(self, data, change):
        if data is not None:
            return self.database.animals.update(data,{ "$set": change})  # data and change are dictionaries
        else:
            print('Nothing to update, because data parameter is empty')
            return False       
            
        #Delete function
     
    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_one(data)  # data is dictionary
        else:
            print('Nothing to delete, because data parameter is empty')
            return False
         
        