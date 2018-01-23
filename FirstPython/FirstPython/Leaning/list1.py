spam = ['cat', 'bat', 'rat' , 'ant']
# get all list
print(spam)
# get by index
print('Get index 1' + spam[1])
# get by slie [start-index:end-index]
print('Get spam slice index 1 to index 3 ',end='')
print(spam[1:3])
# get len of list
print('Len of list: ' + str(len(spam)))
# remove value
del spam[2]
print('Remove index 2',end='')
print(spam);
# in and not in Operators
if 'cat' in spam :
    print('List have cat')
# The Multiple Assignment Trick
pet1,pet2,pet3 = spam
print('List to var :',pet1,pet2,pet3,sep=',')
# Adding Values to Lists with the append() and insert() Methods
# append()
spam.append('moose')
print('Append moose to list',end='')
print(spam,sep=',')
# Insert()
spam.insert(1, 'chicken')
print('Insert index 1 chicken to list',end='')
print(spam,sep=',')
#Removing Values from Lists with remove()
spam.remove('bat')
print('Remove bat from list',end='')
print(spam,sep=',')
#Sorting the Values in a List with the sort() Method
spam.sort(key=str.lower)
print('Sort list',end='')
print(spam,sep=',')
#Test
spam.append(10)
print(spam,sep=',')
#List will only References value
#The copy Module’s copy() and deepcopy() Functions
import copy
cheese = copy.copy(spam)
cheese[1] = 'dog'
print('Copy spam to cheese not referemces :')
print('Cheese is:',end='')
print(cheese,sep=',')
print('Spam is:',end='')
print(spam,sep=',')
