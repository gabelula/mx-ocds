#!/usr/bin/python

# Using http://standard.open-contracting.org/latest/en/schema/release/

from dateutil import parser
import pymongo,urllib, re
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import csv, json

#matplotlib.style.use('ggplot')

# ocid regular expression
ocid_re = re.compile('^OCDS\-87SD3T\-SEFIN\-[a-zA-Z0-9\-]+$')
# language
lang = 'es'

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
tag = {}
published_date = {}
# to calculate buyer completeness
buyer_completeness = {}
# to calculate planning documents & completeness
planning_documents = {}
planning_completeness = {}
# to calculate tender documents & completeness
tender_documents = {}
tender_completeness = {}
award_criteria = {} # stores stats on award criteria
award_period = {}
enquiry_period = {}
has_enquiries = {}
eligibility_criteria = {}
number_of_tenderers = {}
status_tender = {}
procurement_method = {}
items = {}
aitems = {}
citems = {}
units = {}
submission_method = {}
# to calculate award documents & completeness
award_documents = {}
award_completeness = {}
status_award = {}
# to calculate contract documents & completeness
contract_documents = {}
contract_completeness = {}
status_contract = {}

no_planning_documents = 0
no_tender_documents = 0
no_award_documents = 0
no_contract_documents = 0
no_items = 0
tenderperiods = []
values = []

def verify_url(url):
    return (urllib.urlopen(url).getcode() != 200)

def buyer(release):

    total_fields = 5 # do we include additionalidentifiers or not?
    buyer_completeness[release['ocid']] = (len(release['buyer']) * 100 )/ total_fields
    # check identifier uri exists
    if verify_url(release['buyer']['identifier']['uri']):
        print 'Not Found: %s' % release['buyer']['identifier']['uri']

def planning(release):
    global no_planning_documents
    total_fields = 9
    planning_completeness[release['ocid']] = (len(release['planning']) * 100 )/ total_fields
    if release['planning'].has_key('uri'):
        if validate_url(release['planning']['uri']):
            print 'Not Found: %s' % release['planning']['uri']
    # release['planning']['rationale']
    planning_documents[release['ocid']] = 0
    if len(release['planning']['documents']) == 0:
        no_planning_documents = no_planning_documents + 1
    for document in release['planning']['documents']:
        if verify_url(document['url']): # verify that the url exists
            print 'Not Found: %s' %  document['url']
        planning_documents[release['ocid']] = planning_documents[release['ocid']] + 1# how many documents for this release

def tender(release):
    global no_tender_documents
    global no_items
    global tenderperiods
    total_fields = 24
    tender_completeness[release['ocid']] = (len(release['tender']) * 100 )/ total_fields
    tender_documents[release['ocid']] = 0
    if len(release['tender']['documents']) == 0:
        no_tender_documents = no_tender_documents + 1
    for document in release['tender']['documents']:
        if verify_url(document['url']): # verify that the url exists
            print 'Not Found: %s' % document['url']
        tender_documents[release['ocid']] = tender_documents[release['ocid']] + 1# how many documents for this release
    # award criteria for tenders
    if award_criteria.has_key(release['tender']['awardCriteria']):
        award_criteria[release['tender']['awardCriteria']] = award_criteria[release['tender']['awardCriteria']] + 1
    else:
        award_criteria[release['tender']['awardCriteria']] = 0
    award_period[release['ocid']] = release['tender']['awardPeriod'] # when it starts and ends (awardPeriod) ? Are they all already ended?
    if eligibility_criteria.has_key(release['tender']['eligibilityCriteria']):
        eligibility_criteria[release['tender']['eligibilityCriteria']] = eligibility_criteria[release['tender']['eligibilityCriteria']] + 1 # - what is the eligibilityCriteria for the tenders?(grafica de barra)
    else:
        eligibility_criteria[release['tender']['eligibilityCriteria']] = 0
    if release['tender']['enquiryPeriod']['endDate'] != None:
        enquiry_period[release['ocid']] = (parser.parse(release['tender']['enquiryPeriod']['endDate']) - parser.parse(release['tender']['enquiryPeriod']['startDate'])).days# in days how long the enquiryPeriod are?
    else:
        enquiry_period[release['ocid']] = 0
    number_of_tenderers[release['ocid']] = release['tender']['numberOfTenderers'] #  what is the number of tenderers?(grafica de barra)
    if has_enquiries.has_key(release['tender']['hasEnquiries']):
        has_enquiries[release['tender']['hasEnquiries']] = has_enquiries[release['tender']['hasEnquiries']] + 1 # - has enquiries? (grafica de tortas)
    else:
        has_enquiries[release['tender']['hasEnquiries']] = 0
    if status_tender.has_key(release['tender']['status']): # - status? (grafica de barra)
        status_tender[release['tender']['status']] = status_tender[release['tender']['status']] + 1
    else:
        status_tender[release['tender']['status']] = 0
    if procurement_method.has_key(release['tender']['procurementMethod']): # - procurement method (grafica de barra)
        procurement_method[release['tender']['procurementMethod']] = procurement_method[release['tender']['procurementMethod']] + 1
    else:
        procurement_method[release['tender']['procurementMethod']] = 0
    # items (grafica de barra for description)
    # units used in items (grafica de barra)
    if len(release['tender']['items']) == 0:
        no_items = no_items + 1
    for item in release['tender']['items']:
        if items.has_key(item['description']):
            items[item['description']] = items[item['description']] + 1
        else:
            items[item['description']] = 1
        if units.has_key(item['unit']['name']):
            units[item['unit']['name']] = units[item['unit']['name']] + 1
        else:
            units[item['unit']['name']] = 1
    # submission method (grafica de barra)
    for submission in release['tender']['submissionMethod']:
        if submission_method.has_key(submission):
            submission_method[submission] = submission_method[submission]  + 1
        else:
            submission_method[submission] = 0
    tenderperiods.append([release['tender']['tenderPeriod']['startDate'], release['tender']['tenderPeriod']['endDate']])

def award(release):
    global no_award_documents
    global values
    total_fields = 11
    award_documents[release['ocid']] = 0
    award_completeness[release['ocid']] = {}
    for award in release['awards']:
        award_completeness[release['ocid']][award['id']] = (len(award) * 100 )/ total_fields
        award_documents[release['ocid']] = award_documents[release['ocid']] + len(award['documents'])
        if len(award['documents']) == 0 :
            no_award_documents = no_award_documents + 1
        for document in award['documents']:
            verify_url(document['url'])
        if status_award.has_key(award['status']):
            status_award[award['status']] = status_award[award['status']] + 1
        else:
            status_award[award['status']] = 0

        for item in award['items']:
            if aitems.has_key(item['description']):
                aitems[item['description']] = aitems[item['description']] + 1
            else:
                aitems[item['description']] = 1
        #if release['tender']['value']['amount'] > award['value']['amount']:
        values.append([release['ocid'], release['tender']['value']['amount'], award['value']['amount']])

def contract(release):
    global no_contract_documents
    total_fields = 10
    contract_documents[release['ocid']] = 0
    contract_completeness[release['ocid']] = {}
    for contract in release['contracts']:
        contract_completeness[release['ocid']][contract['id']] = (len(contract) * 100 )/ total_fields
        contract_documents[release['ocid']] = contract_documents[release['ocid']] + len(contract['documents'])
        if len(contract['documents']) == 0:
            no_contract_documents = no_contract_documents + 1
        for document in contract['documents']:
            verify_url(document['url'])
        if status_contract.has_key(contract['status']):
            status_contract[contract['status']] = status_contract[contract['status']] + 1
        else:
            status_contract[contract['status']] = 0
        for item in contract['items']:
            if citems.has_key(item['description']):
                citems[item['description']] = citems[item['description']] + 1
            else:
                citems[item['description']] = 1

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


## --------------- MAIN SCRIPT --------------

# Get the mongodb client where to import data into
client = pymongo.MongoClient('localhost', 27017)
db = client.ocds
collection = db.contracts

contracts = collection.find()

p = {}

errors = []

for c in contracts:
    # URLs should be working
    urls = [ c['publisher']['uri'], c['publisher']['scheme'],c['uri']]
    for url in urls:
        if verify_url(url):
            errors.append('Not Found: %s' % url)
    if published_date.has_key(parser.parse(c['publishedDate'])):
        published_date[parser.parse(c['publishedDate'])] = published_date[parser.parse(c['publishedDate'])] + 1
    else:
        published_date[parser.parse(c['publishedDate'])] = 0
    for release in c['releases']:
        print '--------------------- Release %s ---------------------' % release['ocid']
        # format for the OCID by the mx city
        if (ocid_re.match(release['ocid']) == None):
            errors.append('Release %s: OCID not well formed' % release['ocid'])
        # language should always be spanish
        if release['initiationType'] != 'tender': # only tender is supported right now
            errors.append('Release %s: Initiation Type should be tender and not %s'.format(release['ocid'], release['initiationType']))
        # tag specifies what kind of validation we need to do http://standard.open-contracting.org/latest/en/schema/codelists/#release-tag
        for t in release['tag']:
            if tag.has_key(t):
                tag[t] = tag[t] + 1
            else:
                tag[t] = 0
        if 'contract' in release['tag']: # we should have a contract
            if (release['contracts'] == 0):
                errors.append('Release %s: contains contract tag. It should at least have a contract.' % release['ocid'])
        if 'award' in release['tag']: # we should have an award
            if (release['awards'] == 0):
                errors.append('Release %s: contains award tag. It should at least have an award.' % release['ocid'])
        if 'tender' in release['tag']: # we should have an announcing a new tender
            if not release.has_key('tender'):
                errors.append('Release %s: contains tender tag. It should at least have tenders fields.' % release['ocid'])

        # check level of completeness for basic level
        basic, missing_fields = level_basic(release)
        print 'Basic Level: %8.2f complete' % basic
        for m in missing_fields:
            print '\t Missing field: %s' % m

        # buyer
        buyer(release)
        # planning
        planning(release)
        # tender
        tender(release)
        # tender
        award(release)
        # contract
        contract(release)

print '---- BUYER ----'
if len(buyer_completeness) != 0:
    avg = sum(buyer_completeness.values())/len(buyer_completeness)
    print 'Average Completenes %8.2f' % avg

print '---- PLANNING ----'
if len(planning_documents) != 0:
    print 'Average # Documents %8.2f' % (sum(planning_documents.values()) / len(planning_documents) )
print '%d releases have no documents.' % no_planning_documents

if len(planning_completeness) != 0:
    print 'Average Completenes %8.2f' % (sum(planning_completeness.values())/len(planning_completeness))

print '---- TENDER ----'
if len(tender_documents) != 0:
    print 'Average # Documents %8.2f ' % (sum(tender_documents.values())/len(tender_documents))
if len(tender_completeness) != 0:
    print 'Average Completenes %8.2f' % (sum(tender_completeness.values())/len(tender_completeness))

#print status_tender

print '%8.2f releases have no documents' % no_tender_documents
print '%8.2f releases have no items' % no_items
# for i in items:
#     print '%s, %s' % (i, items[i])

print '---- AWARDS ----'
if len(award_documents) != 0:
    print 'Average # Documents %8.2f ' % (sum(award_documents.values())/len(award_documents))
print '%8.2f releases have no documents' % no_award_documents

if len(award_completeness) != 0:
    aw = 0
    for a in award_completeness:
        if len(award_completeness[a]) != 0:
            aw = aw + sum(award_completeness[a].values())/len(award_completeness[a])
    avg = aw/len(award_completeness)
    print 'Average Completenes %8.2f' % avg

# for i in aitems:
#     print '%s, %s' % (i, aitems[i])

print '---- CONTRACTS ----'
if len(contract_documents) != 0:
    print 'Average # Documents %8.2f ' % (sum(contract_documents.values()) / len(contract_documents) )
print '%d releases have no documents' % no_contract_documents
if len(contract_completeness) != 0:
    for c in contract_completeness:
        if len (contract_completeness[a]) != 0:
            print 'Average Completenes %8.2f ' %  (sum(contract_completeness[c].values())/len(contract_completeness[c]))

# for i in citems:
#     print '%s, %s' % (i, citems[i])
# # Summarize to CSV for PLOTTING
# with open('tags.csv', 'w') as csvfile:
#     fieldnames = tag.keys()
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow(tag)
#
# with open('published_dates.csv', 'w') as csvfile:
#     fieldnames = published_date.keys()
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow(published_date)
#
# with open('award_criteria.csv', 'w') as csvfile:
#     fieldnames = award_criteria.keys()
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow(award_criteria)
#
# with open('award_period.csv', 'w') as csvfile:
#     fieldnames = award_period.keys()
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow(award_period)
# enquiry_period = {}
# has_enquiries = {}
# eligibility_criteria = {}
# number_of_tenderers = {}
# status_tender = {}
# procurement_method = {}
# items = {}
# units = {}
# submission_method = {}
# # to calculate award documents & completeness
# award_documents = {}
# award_completeness = {}
# status_award = {}
# # to calculate contract documents & completeness
# contract_documents = {}
# contract_completeness = {}
# status_contract = {}

# PLOTTING

# print tag
# series = pd.Series(tag.keys(), tag.values(), name='tags')
# series.plot(kind='pie', figsize=(6, 6))
# plt.savefig('tags.png', bbox_inches='tight')
