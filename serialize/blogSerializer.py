def Serialize(doc: dict)-> dict:
    return {
        "_id":str(doc["_id"]),
        "email": doc["email"],
        "name": doc["name"],
       "mobile": doc["mobile"]
    }

def SerializeAll(docs)->list:
    return [Serialize(doc) for doc in docs]