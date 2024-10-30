from pymongo import MongoClient

def get_data_from_db():     
    client = MongoClient("mongodb+srv://fredderf:fred555@cluster0.a03do.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client['scrap']
    return db