#!/usr/bin/python

import urllib, json, sys, pymongo, jsonschema, io

## Getting data through GF API: http://www.contratosabiertos.cdmx.gob.mx/api/contratos/todos

url_schema = "http://standard.open-contracting.org/schema/1__0__1/release-package-schema.json"

url_todos = "http://www.contratosabiertos.cdmx.gob.mx/api/contratos/todos"
url_per_contrato = "http://www.contratosabiertos.cdmx.gob.mx/api/contrato/{ocid}"

# Get the schema to validate
response = urllib.urlopen(url_schema)
schema = json.loads(response.read())

# Get all the contracts
response = urllib.urlopen(url_todos)
contracts = json.loads(response.read())

# Get the mongodb client where to import data into
client = pymongo.MongoClient('localhost', 27017)
db = client.ocds
collection = db.contracts

for c in contracts:
    ocid = c['ocdsid']

    # Get the contract
    uri = url_per_contrato.format(ocid=ocid)
    ocid_name = "{ocid}.json".format(ocid=ocid)

    rc = urllib.urlopen(uri)
    contract = json.loads(rc.read())

    # # Write it into json file
    # print "Writing contract %s as a json file." % ocid
    #
    # try:
    #     with io.open(ocid_name, 'w', encoding='utf-8') as f:
    #         f.write(unicode(json.dumps(contract, ensure_ascii=False)))
    # except TypeError:
    #     print "Type Error({0})".format(sys.exc_info()[1])
    # except IOError as e:
    #     print "I/O error({0}): {1}".format(e.errno, e.strerror)
    # except:
    #     print "Error when writing contract: {0}, {1}".format(sys.exc_info()[0], sys.exc_info()[1])

    # # Insert it into mongodb
    # c_id = collection.insert_one(contract).inserted_id
    # print "Import contract %s into MongoDB collection, with id %s." % (ocid, c_id)

    # Validate that it works
    print "Validating contract %s:" % ocid
    try:
        if jsonschema.validate(contract, schema) == None:
            print "Succesful"
    except jsonschema.exceptions.ValidationError as e:
        print "\tValidation Error({0}): field {1}, value {2}, instance {3}".format(e.message, e.validator, e.validator_value, e.instance)
        print dir(e)
