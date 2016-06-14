#!/usr/local/bin/python3

import json, pymongo, glob

def write_to_mongo(ocid, contract, collection):
    # Insert it into mongodb
    c_id = collection.insert_one(contract).inserted_id
    print(ocid, c_id)

def main():
    # Get the mongodb client where to import data into
    client = pymongo.MongoClient('localhost', 27017)
    db = client.ocds
    collection = db.contracts

    for filename in glob.glob('data/*.json'):
        with open(filename) as fp:
            contract = json.load(fp)
            ocid = contract['releases'][0]['ocid']
            write_to_mongo(ocid, contract, collection)

if __name__ == "__main__":
    main()
