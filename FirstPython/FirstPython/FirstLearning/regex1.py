import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
getPhone = phoneNumRegex.search('My number is 415-555-4242.')

print('Phone number found: ' + getPhone.group())
print('----------------------------')
#Grouping with Parentheses
print('Group is 1:',getPhone.group(1))
print('Group is 2:',getPhone.group(2))
print('Group is 0:',getPhone.group(0))
print('Group all:',getPhone.groups())
print('----------------------------')
#groups return tuple to var
areaCode, mainNumber = getPhone.groups()
print(areaCode)
print(mainNumber)
print('----------------------------')
#regex with pipe |
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
print('----------------------------')
#Optional Matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
print('----------------------------')
#Matching One or More with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)
print('----------------------------')
#The findall() Method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))