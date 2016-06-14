import simplejson
from numpy import genfromtxt

class CompanyName():

    def __init__(self, csvRowAsList, headerMap):
        self.companyName = csvRowAsList[headerMap['Company Name']]
        self.executiveName = csvRowAsList[headerMap["Executive Name"]]

    def getCompanyName(self):
        return self.companyName

    def getExecutiveName(self):
        return self.executiveName

    def companyNameMatches(self):
        pass

    def __str__(self):
        return str({ "company_name": self.companyName, "executiveName": self.executiveName })

class CompanyTwitterAccount():
    def __init__(self, company, user):
        self.company = company
        self.profileUrl = generateProfilePageUrl(user)
        self.numTweets = user['retweet_count'] # not really sure that this exists
        self.numFollowers = user['followers_count']
        self.numFavorites = user['favourites_count']

json_file = open("chase_search_results.json", 'r')
jsonResponse = simplejson.load(json_file)

for user in jsonResponse:
    data = {'default_profile': user['default_profile'], 'id': user['id'],  'name': user['name'], 'screen_name': user['screen_name'] }
    print data
    print

def matchNameToCompany(company, name):
    if name.lower() == company.executiveName.lower():
        return True
    elif name.lower() == company.companyName.lower():
        return True
    else: # need some slightly looser definition of matching
        return False

csvFileName = 'test.csv'
print "Reading in CSV from " + csvFileName
with open(csvFileName, 'r') as csvfile:
    data = genfromtxt(csvfile, delimiter=',', dtype=None)
    headerMap = dict(zip(data[0], xrange(0,len(data[0]))))
    foundCompanies = []
    for row in data[1:]:
        companyName = CompanyName(row, headerMap)
        print companyName
        # TODO: Make request to twitter here
        requestList = None
        for user in requestList:
            if matchNameToCompany(companyName, user):
                foundCompanies.append(CompanyTwitterAccount(companyName))

# TODO: write out twitter data
destinationCsvFileName = None
for twitterAccount in foundCompanies:
    pass

def generateProfilePageUrl(user):
    return 'https://twitter.com/' + user['screen_name']