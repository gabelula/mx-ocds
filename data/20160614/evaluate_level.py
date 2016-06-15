#!/usr/local/bin/python3

# Using http://standard.open-contracting.org/latest/en/schema/release/

import pymongo, json, io

def level_basic(basic_fields, release):
    basic_values_file = 'intermediate.json'
    basic_values = {}
    total_fields = 0
    completed_fields = 0
    missing_fields = []
    for i in basic_fields:
        if i in release:
            for f in basic_fields[i]: # basic_fields[i] is always a list
                if type(f) is dict: # for example {"tenderers": [ "identifier" ] }
                    for p in f:
                        if type(f[p]) is list:
                            for j in f[p]:
                                if (p in release[i]):
                                    if (type(release[i][p]) is list):
                                        #found = False
                                        if type(j) == str:
                                            total_fields = total_fields + 1
                                            for x in release[i][p]:
                                                if j in x:
                                                    #found = True
                                                    completed_fields = completed_fields + 1
                                                    k = i + '.' + p + '.' + j
                                                    basic_values[k] = x[j]
                                                    break
                                            else:
                                                missing_fields.append(i + '.' + p + '.' + j)
                                        elif type(j) == dict:
                                            for m in j:
                                                total_fields = total_fields + 1
                                                for x in release[i][p]:
                                                    if m in x:
                                                        #found = True
                                                        completed_fields = completed_fields + 1
                                                        k = i + '.' + p + '.' + m
                                                        basic_values[k] = x[m]
                                                        break
                                                else:
                                                    missing_fields.append(i + '.' + p + '.' + m)

                                    if (type(release[i][p]) is dict):
                                        if type(j) == str:
                                            total_fields = total_fields + 1
                                            for x in release[i][p]:
                                                if x == j:
                                                    completed_fields = completed_fields + 1
                                                    k = i + '.' + p + '.' + j
                                                    basic_values[k] = release[i][p][x]
                                                    break
                                            else:
                                                missing_fields.append(i + '.' + p + '.' + j)
                                        elif type(j) == dict:
                                            for key in j:
                                                total_fields = total_fields + 1
                                                if key in release[i][p]:
                                                    completed_fields = completed_fields + 1
                                                    k = i + '.' + p + '.' + key
                                                    basic_values[k] = release[i][p][x]
                                                else:
                                                    missing_fields.append(i + '.' + p + '.' + key)
                                else:
                                    total_fields = total_fields + 1
                                    missing_fields.append(i + '.' + p)
                else: # for example "title"
                    total_fields = total_fields + 1
                    if f in release[i]:
                        completed_fields = completed_fields + 1
                        k = i + '.' +  f
                        basic_values[f] = release[i][f]
                    else:
                        missing_fields.append(i + '.' + f)

    completeness = (completed_fields*100)/total_fields

    # write all the fields for basic implementation
    # bvf = release['ocid'] +'_' + basic_values_file
    # with open(bvf, 'w') as outfile:
    #     json.dumps(basic_values, outfile)

    return completeness, missing_fields

def main():
    # Get the mongodb client where to import data into
    client = pymongo.MongoClient('localhost', 27017)
    db = client.ocds
    collection = db.contracts

    contracts = collection.find()


    with open('intermediate_fields.json', 'r') as outfile:
        basic_fields = json.load(outfile)

    report = io.open('eval_intermediate.json', 'w', encoding='utf-8')

    for c in contracts:
        for release in c['releases']:
            r = {}
            r['ocid'] = release['ocid']
            # amount of items
            ti = len(release['tender']['items'])
            ai = 0
            ci = 0
            for a in release['awards']:
                 ai = ai + len(a['items'])
            for con in release['contracts']:
                ci = ci + len(con['items'])
            if ti != ai or ai != ci :
                print(release['ocid'],' ITEMS IN Tender: ' , ti , ' Awards: ' , ai , ' Contract: ' , ci )
            r['missing'] = []
            # check level of completeness for basic level
            basic, missing_fields = level_basic(basic_fields, release)
            r['completeness'] = basic
            #print('Intermediate Level for ', release['ocid'],': ', basic, ' complete')
            for m in missing_fields:
                #print('\t Missing field: ', m)
                r['missing'].append(m)
            report.write(json.dumps(r, ensure_ascii=False))

if __name__ == "__main__":
    main()
