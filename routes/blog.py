import datetime
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from models.schema import UserSchema,UpdateUserSchema
from config.config import CrudCollection
from serialize.blogSerializer import SerializeAll,Serialize

root = APIRouter()

@root.post('/insert')
async def addData(doc:UserSchema):
    doc = dict(doc)
    current_date = datetime.date.today()
    print(str(current_date),'this is the date')
    res = CrudCollection.insert_one(doc)
    gen_id = str(res.inserted_id)
    data = Serialize(doc)
    return {
        "status":"data insertion success",
        "_id": gen_id,
        "data":data
    }

@root.get('/all')
async def getData():
    res = CrudCollection.find()
    serial_data = SerializeAll(res)
    return serial_data

@root.get('/{id}')
async def byId(id:str):
    res = CrudCollection.find_one({"_id":ObjectId(id)})
    serial_data = Serialize(res)
    return serial_data

@root.patch('/{id}')
async def update(id: str, doc: UpdateUserSchema):
    update_data = doc.dict(exclude_unset=True) 
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    result = CrudCollection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Document not found")
    updated_document = CrudCollection.find_one({"_id": ObjectId(id)})
    serial_data = Serialize(updated_document)
    return {
        "status": "update success",
        "data": serial_data
    }
  
@root.delete('/{id}')
async def deleteFun(id:str):
    res = CrudCollection.delete_one({"_id":ObjectId(id)})
    return {
        "message":"delete Successfull"
    } 