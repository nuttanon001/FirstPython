import json

# write
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

# read
numbersRead = []
with open(filename) as file_obj:
    numbersRead = json.load(file_obj)

print(numbersRead)

