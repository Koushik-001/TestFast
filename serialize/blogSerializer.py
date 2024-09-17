def Serialize(doc):
    return {
        "_id": str(doc.get("_id")),
        "name": doc.get("name", ""),  # Use .get() to provide a default value
        "email": doc.get("email", ""),
        "mobile": doc.get("mobile", ""),  # Handle missing 'mobile' key
    }


def SerializeAll(docs)->list:
    return [Serialize(doc) for doc in docs]