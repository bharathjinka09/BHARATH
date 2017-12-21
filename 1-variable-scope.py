'''
def outer_function():
    b = 20
    print("a :", a)
    print("b :", b)
    def inner_func():
        c = 30
        print("a :", a)
        print("b :", b)
        print("c :", c)
    inner_func()
    #print ("c :", c)

a = 10
outer_function()
print("a :", a)
#print("b :", b)
#print("c :", c)
exit(1)
'''

'''
def outer_function():
    a = 20
    b = 20
    print("a :", a)
    print("b :", b)
    def inner_function():
        a = 30
        c = 30
        print("a :", a)
        print("b :", b)
        print("c :", c)

    inner_function()
    print ("a :", a)
     
a = 10
outer_function()
print ("a :", a)
'''

'''
def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print(('a :',a))

    inner_function()
    print(('a :',a))
     
a = 10
outer_function()
print(('a :',a))
exit(1)
'''
