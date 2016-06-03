#!/usr/bin/python

# Using http://standard.open-contracting.org/latest/en/schema/release/

import pymongo, json

basic_fields = { "buyer" : ["address", "name"],
                "tender" : [ {"tenderers": [ "identifier" ] }, "title", "description",
                             "status", "procurementMethod", "awardPeriod",
                             {"items": ["description", "quantity"]}, "documents"
                            ],
                "award" : [ "id", "title", "description", "date", "value",
                            { "supplier": [ "name" , "address"]}
                          ],
                "contract" : [ "id", "title", "status", "period", "value",
                               { "items": ["description", "quantity"]}
                             ]
                }

def level_basic(release):
    basic_values_file = 'basic.json'
    basic_values = {}
    total_fields = 0
    completed_fields = 0
    missing_fields = []
    for i in basic_fields:
        if release.has_key(i):
            for f in basic_fields[i]: # basic_fields[i] is always a list
                if type(f) is dict: # for example {"tenderers": [ "identifier" ] }
                    for p in f:
                        if type(f[p]) is list:
                            for j in f[p]:
                                if type(release[i][p]) is list:
                                    total_fields = total_fields + 1
                                    found = False
                                    for x in release[i][p]:
                                        if x[j]:
                                            found = True
                                            completed_fields = completed_fields + 1
                                            k = i + '.' + p + '.' + j
                                            basic_values[k] = x[j]
                                            break
                                    if not found :
                                        missing_fields.append("Field not found %s" % j)
                                else:
                                    print "YEAH???"
                else: # for example "title"
                    total_fields = total_fields + 1
                    if release[i].has_key(f):
                        completed_fields = completed_fields + 1
                        k = i + '.' +  f
                        basic_values[f] = release[i][f]
                    else:
                        missing_fields.append("Field not found: %s" % f)

    completeness = (completed_fields*100)/total_fields

    # write all the fields for basic implementation
    bvf = release['ocid'] +'_' + basic_values_file
    with open(bvf, 'w') as outfile:
        json.dumps(basic_values, outfile)

    return completeness, missing_fields

def main():
    # Get the mongodb client where to import data into
    client = pymongo.MongoClient('localhost', 27017)
    db = client.ocds
    collection = db.contracts

    contracts = collection.find()

    for c in contracts:
        for release in c['releases']:
            # check level of completeness for basic level
            basic, missing_fields = level_basic(release)
            print 'Basic Level: %8.2f complete' % basic
            for m in missing_fields:
                print '\t Missing field: %s' % m

if __name__ == "__main__":
    main()
