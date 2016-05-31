#!/usr/bin/python

# Using http://standard.open-contracting.org/latest/en/schema/release/

from dateutil import parser
import pymongo,urllib, re
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import csv

#matplotlib.style.use('ggplot')

# ocid regular expression
ocid_re = re.compile('^OCDS\-87SD3T\-SEFIN\-[a-zA-Z0-9\-]+$')
# language
lang = 'es'
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

def verify_url(url):
    return (urllib.urlopen(url).getcode() != 200)

def buyer(release):

    total_fields = 5 # do we include additionalidentifiers or not?
    buyer_completeness[release['ocid']] = (len(release['buyer']) * 100 )/ total_fields
    # check identifier uri exists
    if verify_url(release['buyer']['identifier']['uri']):
        print 'Not Found: %s' % release['buyer']['identifier']['uri']

def planning(release):
    total_fields = 9
    planning_completeness[release['ocid']] = (len(release['planning']) * 100 )/ total_fields
    if release['planning'].has_key('uri'):
        if validate_url(release['planning']['uri']):
            print 'Not Found: %s' % release['planning']['uri']
    # release['planning']['rationale']
    planning_documents[release['ocid']] = 0
    for document in release['planning']['documents']:
        if verify_url(document['url']): # verify that the url exists
            print 'Not Found: %s' %  document['url']
        planning_documents[release['ocid']] = planning_documents[release['ocid']] + 1# how many documents for this release

def tender(release):
    total_fields = 24
    tender_completeness[release['ocid']] = (len(release['tender']) * 100 )/ total_fields
    tender_documents[release['ocid']] = 0
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
    for item in release['tender']['items']:
        if items.has_key(item['description']):
            items[item['description']] = items[item['description']] + 1
        else:
            items[item['description']] = 0
        if units.has_key(item['unit']['name']):
            units[item['unit']['name']] = units[item['unit']['name']] + 1
        else:
            units[item['unit']['name']] = 0
    # submission method (grafica de barra)
    for submission in release['tender']['submissionMethod']:
        if submission_method.has_key(submission):
            submission_method[submission] = submission_method[submission]  + 1
        else:
            submission_method[submission] = 0

def award(release):
    total_fields = 11
    award_documents[release['ocid']] = 0
    award_completeness[release['ocid']] = {}
    for award in release['awards']:
        award_completeness[release['ocid']][award['id']] = (len(award) * 100 )/ total_fields
        award_documents[release['ocid']] = award_documents[release['ocid']] + len(award['documents'])
        for document in award['documents']:
            verify_url(document['url'])
        if status_award.has_key(award['status']):
            status_award[award['status']] = status_award[award['status']] + 1
        else:
            status_award[award['status']] = 0

def contract(release):
    total_fields = 10
    contract_documents[release['ocid']] = 0
    contract_completeness[release['ocid']] = {}
    for contract in release['contracts']:
        contract_completeness[release['ocid']][contract['id']] = (len(contract) * 100 )/ total_fields
        contract_documents[release['ocid']] = contract_documents[release['ocid']] + len(contract['documents'])
        for document in contract['documents']:
            verify_url(document['url'])
        if status_contract.has_key(contract['status']):
            status_contract[contract['status']] = status_contract[contract['status']] + 1
        else:
            status_contract[contract['status']] = 0



## --------------- MAIN SCRIPT --------------

# Get the mongodb client where to import data into
client = pymongo.MongoClient('localhost', 27017)
db = client.ocds
collection = db.contracts

contracts = collection.find()

p = {}
for c in contracts:
    # URLs should be working
    urls = [ c['publisher']['uri'], c['publisher']['scheme'],c['uri']]
    for url in urls:
        if verify_url(url):
            print 'Not Found: %s' % url
    if published_date.has_key(parser.parse(c['publishedDate'])):
        published_date[parser.parse(c['publishedDate'])] = published_date[parser.parse(c['publishedDate'])] + 1
    else:
        published_date[parser.parse(c['publishedDate'])] = 0
    for release in c['releases']:
        print '--------------------- Release %s ---------------------' % release['ocid']
        # format for the OCID by the mx city
        if (ocid_re.match(release['ocid']) == None):
            print 'Release %s: OCID not well formed' % release['ocid']
        # language should always be spanish
        if release['initiationType'] != 'tender': # only tender is supported right now
            print 'Release %s: Initiation Type should be tender and not %s'.format(release['ocid'], release['initiationType'])
        # tag specifies what kind of validation we need to do http://standard.open-contracting.org/latest/en/schema/codelists/#release-tag
        for t in release['tag']:
            if tag.has_key(t):
                tag[t] = tag[t] + 1
            else:
                tag[t] = 0
        if 'contract' in release['tag']: # we should have a contract
            if (release['contracts'] == 0):
                print 'Release %s: contains contract tag. It should at least have a contract.' % release['ocid']
        if 'award' in release['tag']: # we should have an award
            if (release['awards'] == 0):
                print 'Release %s: contains award tag. It should at least have an award.' % release['ocid']
        if 'tender' in release['tag']: # we should have an announcing a new tender
            if not release.has_key('tender'):
                print 'Release %s: contains tender tag. It should at least have tenders fields.' % release['ocid']

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
planning_documents.values()
if len(planning_documents) != 0:
    print 'Average # Documents %d' % (sum(planning_documents.values())/len(planning_documents))
if len(planning_completeness) != 0:
    print 'Average Completenes %8.2f' % (sum(planning_completeness.values())/len(planning_completeness))

print '---- TENDER ----'
if len(tender_documents) != 0:
    print 'Average # Documents %d ' % (sum(tender_documents.values())/len(tender_documents))
if len(tender_completeness) != 0:
    print 'Average Completenes %8.2f' % (sum(tender_completeness.values())/len(tender_completeness))

print '---- AWARDS ----'
if len(award_documents) != 0:
    print 'Average # Documents %d ' % (sum(award_documents.values())/len(award_documents))
if len(award_completeness) != 0:
    for a in award_completeness:
        if len (award_completeness[a]) != 0:
            print 'Average Completenes %8.2f' %  (sum(award_completeness[a].values())/len(award_completeness[a]))

print '---- CONTRACTS ----'
if len(contract_documents) != 0:
    print 'Average # Documents %d ' % (sum(contract_documents.values())/len(contract_documents))
if len(contract_completeness) != 0:
    for c in contract_completeness:
        if len (contract_completeness[a]) != 0:
            print 'Average Completenes %8.2f ' %  (sum(contract_completeness[c].values())/len(contract_completeness[c]))

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
