class MyClass:
	name = "bhagavan"
	x = 0
	y = 0

	def __init__(self):
		self.name = ""
		self.x = 1
		self.y = 1
		print("1. In constructure function")

	def print_data(self):
		print("In print_data function in class")
		print (name)

	def store_data(self, data):
		print("In store_data function in class")
		name = data

	def get_data(self):
		print("In get_data function in class")
		return self.name

def main():
	obj1 = MyClass()
	print((obj1.get_data()))

	return

if (__name__ == "__main__"):
	main()

