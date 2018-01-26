import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
#Get Type
print(type(res))
#Get Status
print(res.status_code == requests.codes.ok)
#Get len
print(len(res.text))
#Show Text
print(res.text[:250])


import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()