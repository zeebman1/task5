import requests
from json import loads
from random import getrandbits

a = ("%032x" % getrandbits(128))[:14]
def registerUser(local=False, a=a, debug=False):
    ip = '127.0.0.1' if local else '167.172.148.225'
    ip += ':5000' if debug and local else ''
    url = 'http://{}/'.format(ip)
    print(url)
    a += 'b'; loggedIn = requests.post(url+'user/', json={'username': a, 'email': a, 'password': a}).text
    headers = {'Authorization': loads(loggedIn)['Authorization'].encode()};
    location = requests.get(url+'location', headers=headers).text
    print('\n\n', location, '\n\n')
    location = loads(location)

    return loggedIn, location

r = registerUser(local=True, debug=False)
print(r[1])
