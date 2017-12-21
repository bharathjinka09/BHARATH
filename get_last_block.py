fd = open("dhcpd.conf", "r")
i = 0

data = fd.readlines()

print (data)

for line in data:
	#print (line)
	if (line.find("{") >= 0):
		print (line)

for line in data:
	if (line.find("}") >= 0):
		print (line)
for line in data:
	print ("%d. %s" % (i, line))
	i = i + 1


print (data[26])
print (data[26].strip().split(" "))
