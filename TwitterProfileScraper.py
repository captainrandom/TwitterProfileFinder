from TwitterAPI import TwitterAPI
import urllib
import json

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


queryStr = "chase"
encodedStr = urllib.quote(queryStr)
r = api.request('users/search', {'q': encodedStr})
print r.status_code
print r.response
print r.text

jsonResponse = json.loads(r.text)

json_file = open("chase_search_results.json", 'w')
json.dump(jsonResponse, json_file)

print len(jsonResponse)
for user in jsonResponse:
    print json.dumps(user)