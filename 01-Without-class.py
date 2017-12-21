a = 10

def get_data():
    global a
    #print "a :", a
    return a

def set_data(n):
    global a
    #print "a :", a
    a = n
    return a

def dump_data():
    global a
    print(("a :", a))

def increment_data(n):
    global a
    a = a + n
    #print "a :", a

def main():
	global a
	print(("data :", get_data()))

	increment_data(10)

	print(("data :", get_data()))

	increment_data(20)

	dump_data()

	print(("data :", get_data()))
	a = 100
	print(("data :", get_data()))

if (__name__ == "__main__"):
	main()
