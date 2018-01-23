def spam():
    global eggs # Set eggs is var from global
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
