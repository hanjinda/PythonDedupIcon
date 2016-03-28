import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
class Database:
    def __init__(self):
        try:
            client = MongoClient()
            print "Connected successfully!!!"
        except pymongo.errors.ConnectionFailure, e:
           print "Could not connect to MongoDB: %s" % e
        db = client['element_data']
        self.table = db["images_in_session"]


    def set_images_for_session(self, session_id, images):
        return self.table.find({"session_id": session_id}).distinct("image_id")


    def save_images_for_session(self, session_id, images):
        print session_id
        print images

        self.table.update_one(
            {"_id" : ObjectId(session_id)},
            {"$set":{"_id" : ObjectId(session_id), "images": images}}, # change to ObjectId(parent_element_id)}},
            upsert=True
        )