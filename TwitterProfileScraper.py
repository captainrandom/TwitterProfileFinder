import twitter

# TODO import this from a file!
credentials = {
    consumer_key: 'wlGwrADmtrQ2yV6k4wtHbMvid',
    consumer_secret: '9gfZvy9hs6ggIxc2H3xA9pGcJC7AWAx7TA1EbblfHgKV6FHw4C',
    access_token_key: '	3092672244-ZG8dHKNlHNzv894c0ac6539TXBXio5zJrjevFZM'
}

api = twitter.Api(consumer_key='consumer_key',
                  consumer_secret='consumer_secret',
                  access_token_key='access_token',
                  access_token_secret='access_token_secret')