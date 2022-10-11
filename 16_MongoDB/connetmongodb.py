import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodbakshay:Akshay1000#@cluster0.0206nhg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)


dict = {
    'First name' : 'Akshay',
    'Last name' : 'Raj'
}

dict2 = {
    'College' : 'St Stephens college',
    'City' : 'New Delhi'
}


db1 = client['mongotest']
coll = db1['test']
coll.insert_one(dict)