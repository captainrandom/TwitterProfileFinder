from TwitterAPI import TwitterAPI
import urllib
import json
import os.path
from CompanyData import CompanyTwitterAccount, CompanyName


# TODO: Clean up this method
def queryTwitter(queryStr):
    if os.path.isfile(queryStr + "_search_result.json"):
        with open(queryStr + "_search_result.json") as jsonFile:
            jsonResponse = json.load(jsonFile)
    else:
        encodedStr = urllib.quote(queryStr)
        r = api.request('users/search', {'q': encodedStr})
        print r.text
        jsonResponse = json.loads(r.text)

        # cache the results  to a file so that we can use it later.
        with open("chase_search_results.json", 'w') as json_file:
            json.dump(jsonResponse, json_file)

        # print out results
        print len(jsonResponse)
        for user in jsonResponse:
            print json.dumps(user)

    return jsonResponse

import csv
def saveResultsToCsv(companyTwitterAccountList, destinationCsvFileName='output.csv'):
    print "num companies found " + str(len(companyTwitterAccountList))
    print "Writing results to " + destinationCsvFileName
    with open(destinationCsvFileName, 'w') as fp:
        writer = csv.writer(fp, delimiter=',')
        if len(foundCompanies) > 0:
            writer.writerows([foundCompanies[0].getHeader()])
        data = [twitterAccount.asList() for twitterAccount in companyTwitterAccountList]
        writer.writerows(data)


from numpy import genfromtxt
def readInCsvFile(csvFileName):
    print "Reading in CSV from " + csvFileName
    with open(csvFileName, 'r') as csvfile:
        # build header info
        data = genfromtxt(csvfile, delimiter=',', dtype=None)
        headerMap = dict(zip(data[0], xrange(0,len(data[0]))))

        for row in data[1:]:
            # read in data about each company
            yield CompanyName(row, headerMap)

# There might be a better place for these methods

def matchUserToCompany(company, user):
    listOfAttributesToCheck = ['screen_name', 'name']
    for attribute in listOfAttributesToCheck:
        if matchNameToCompany(company, user[attribute]):
            return True
    return False

def matchNameToCompany(company, name):
    if name.lower() == company.getExecutiveName().lower():
        return True
    elif name.lower() == company.getCompanyName().lower():
        return True
    else: # need some slightly looser definition of matching
        return False

def findAndBuildTwitterCompnayAccount(companyName, userList):
    for user in userList:
            if matchUserToCompany(companyName, user):
                return CompanyTwitterAccount(companyName, user)


# TODO import this from a file!
credentials = {
    'consumer_key': 'wlGwrADmtrQ2yV6k4wtHbMvid',
    'consumer_secret': '9gfZvy9hs6ggIxc2H3xA9pGcJC7AWAx7TA1EbblfHgKV6FHw4C',
    'access_token_key': '3092672244-ZG8dHKNlHNzv894c0ac6539TXBXio5zJrjevFZM',
    'access_token_secret': 'wMJBDmG2CXDWMtNaNHO0VfGNq6ZfL7h5tApCBAxMLl1mk'
}

api = TwitterAPI(credentials['consumer_key'],
                  credentials['consumer_secret'],
                  credentials['access_token_key'],
                  credentials['access_token_secret'])


foundCompanies = []
for company in readInCsvFile('test.csv'):
    companyUsrList = queryTwitter(company.getCompanyName()) # TODO: need to make sure of the format for both
    ceoUserList = queryTwitter(company.getExecutiveName())

    # need to find a a way to combine these later.
    companyTwitterAccount = findAndBuildTwitterCompnayAccount(company, companyUsrList)
    ceoTwitterAccount = findAndBuildTwitterCompnayAccount(company, ceoUserList)
    if companyTwitterAccount:
        foundCompanies.append(companyTwitterAccount)

saveResultsToCsv(foundCompanies, 'output.csv')