class CompanyName():

    def __init__(self, csvRowAsList, headerMap):
        self.companyName = csvRowAsList[headerMap['Company Name']].strip()
        self.executiveName = csvRowAsList[headerMap["Executive Name"]].strip()

    def getCompanyName(self):
        return self.companyName

    def getExecutiveName(self):
        return self.executiveName

    def companyNameMatches(self):
        pass

    def __str__(self):
        return str({ "company_name": self.companyName, "executiveName": self.executiveName })


def generateProfilePageUrl(user):
    return 'https://twitter.com/' + user['screen_name']

class CompanyTwitterAccount():
    def __init__(self, company, user):
        self.company = company
        self.profileUrl = generateProfilePageUrl(user)
        self.numTweets = user['statuses_count'] # not really sure that this exists
        self.numFollowers = user['followers_count']
        self.numFavorites = user['favourites_count']

    def asList(self):
        return [self.company.getCompanyName(), self.company.getExecutiveName(), self.profileUrl, self.numTweets, self.numFollowers,
                self.numFavorites]

    def getHeader(self):
        return ["Company Name", "Executive Name", "Profile Url", "Num Tweets", "Num Followers", "Num Favorites"]
