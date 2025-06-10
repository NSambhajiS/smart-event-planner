from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from pymongo import ReturnDocument

DATABASE_URL = "your_mongodb_atlas_connection_string"
DATABASE_NAME = "your_database_name"

client = AsyncIOMotorClient(DATABASE_URL)
database = client[DATABASE_NAME]

async def get_collection(collection_name):
    return database[collection_name]

async def create_document(collection_name, document):
    collection = await get_collection(collection_name)
    result = await collection.insert_one(document)
    return str(result.inserted_id)

async def read_document(collection_name, document_id):
    collection = await get_collection(collection_name)
    document = await collection.find_one({"_id": ObjectId(document_id)})
    return document

async def update_document(collection_name, document_id, update_data):
    collection = await get_collection(collection_name)
    updated_document = await collection.find_one_and_update(
        {"_id": ObjectId(document_id)},
        {"$set": update_data},
        return_document=ReturnDocument.AFTER
    )
    return updated_document

async def delete_document(collection_name, document_id):
    collection = await get_collection(collection_name)
    result = await collection.delete_one({"_id": ObjectId(document_id)})
    return result.deleted_count > 0