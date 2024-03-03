from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user='aacuser', passwd='snhu1234'):
        # Initializing the MongoClient. 
        # This helps to access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the animals collection, 
        # and the aac user.

        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
    
        # Connection Variables
        USER = 'aacuser'
        PASS = 'snhu1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32717
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user,passwd,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
    # get total amount of docs in the database:
    def getTotalDocs(self):
        return self.database.animals.count_documents({})
    
    # Create method to implement the C in CRUD
    # Takes a dictionary (key, value pairs) and inserts it into database/collection
    # Will return True if creation was successful and false if not
    def create(self, data):
        if data is not None and isinstance(data,dict):
            self.database.animals.insert_one(data)  # data should be dictionary
            return True            
        else:
            raise Exception("Nothing to save, because data parameter is empty or incorrect!")
            return False

    # Read method to implement the R in CRUD
    # Takes dictionary (key, value pairs) and finds it in database/collection
    # i.e. {"address":"1234 snhu Rd"}
    # Returns a list if the collection was found else ot returns an empty list
    def read(self, data):
        if data is not None and isinstance(data,dict):
            foundData = list(self.database.animals.find(data))     
        else:
            raise Exception("Nothing was found, because data parameter is empty or incorrect!")

        # this will return an empty list if no data matched or data was empty
        return foundData
    
    # Update method to implement the U in CRUD
    # query = dictionary (key, value pairs) and finds it in database/collection - i.e. {"address":"1234 snhu Rd"}
    # newData = dictionary (key, value pairs) and updates values with newData in database/collection for all found query instances
    # Returns an int of amount of docs that were updated
    def update(self, query, newData):
        foundData = []
        
        if query is not None and newData is not None and isinstance(query,dict) and isinstance(newData,dict):
            foundData = list(self.database.animals.find(query))
            updateData = {"$set":newData} # set is keyword to update the data
            self.database.animals.update_many(query,updateData)
        else:
            raise Exception("Nothing was updated, because data parameter is empty or incorrect!")
        
        return len(foundData)
        
    # Delete method to implement the D in CRUD
    # Takes dictionary (key, value pairs) and finds and deletes it in database/collection
    # i.e. {"address":"1234 snhu Rd"}
    # Returns a string that tells you how many docs were deleted
    def delete(self, data):
        foundData = []
        
        if data is not None and isinstance(data,dict):
            foundData = list(self.database.animals.find(data))
            self.database.animals.delete_many(data)
        else:
            raise Exception("Nothing was deleted, because data parameter is empty or incorrect!")

        return len(foundData)

