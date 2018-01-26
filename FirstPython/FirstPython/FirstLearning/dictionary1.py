myCat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
    }

print('All dictionary',myCat,sep=';')
# get item
for item in myCat.items():
    print('All items is:',item)
# get value
for value in myCat.values():
    print('Value is',value)
# get key
for key in myCat.keys():
    print('Key is',key)

print('--------------------------------')
# get key and value

for key, value in myCat.items():
    print('Key: ' + key + ' Value: ' + str(value))
print('--------------------------------')
#The get() Method from dictionary get(key name,if none value)
print('Key is disposition','Value is',str(myCat.get('disposition', 'none value')))
print('Key is a1','Value is',str(myCat.get('a1', 'none value')))

print('--------------------------------')
#The setdefault() Method for key no value and use pprint
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count)
print('--------------------------------')
print(pprint.pformat(count))
