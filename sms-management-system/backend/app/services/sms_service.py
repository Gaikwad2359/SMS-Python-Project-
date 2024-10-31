from app.models.config import config_collection

def add_country_operator(country, operator, high_priority):
    config_collection.insert_one({
        "country": country,
        "operator": operator,
        "high_priority": high_priority,
        "active": True
    })

def remove_country_operator(pair_id):
    config_collection.delete_one({"_id": pair_id})

def update_country_operator(pair_id, success_rate):
    config_collection.update_one(
        {"_id": pair_id},
        {"$set": {"success_rate": success_rate}}
    )
