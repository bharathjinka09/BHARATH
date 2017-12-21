'''
host marketing-desktop {
        hardware ethernet C0:25:E9:26:81:B2;
        fixed-address 192.168.1.215;
        option routers 192.168.1.1;
}
''' 

def get_new_dhcp_rule2(sysname, macaddr, newip):
	newblock = ""
	newblock = newblock + "host %s  {\n" % (sysname)
	newblock = newblock + ("\thardware ethernet %s;\n" % macaddr)
	newblock = newblock + ("\tfixed-address %s;\n" % (newip))
	newblock = newblock + ("\tfixed-address %s;\n" % (newip))
	newblock = newblock + ("\toption routers 192.168.1.1;\n }\n")

	return (newblock)
	
def get_new_dhcp_rule1(sysname, macaddr, newip):
	blockname = "host %s  {" % (sysname)
	print (blockname)
	newblock = ""
	newblock = newblock + blockname + "\n"

	hwline = ("\thardware ethernet %s;" % macaddr)
	print (hwline)
	newblock = newblock + hwline + "\n"

	fix_addr = ("\tfixed-address %s;" % (newip))
	print (fix_addr)
	newblock = newblock + fix_addr + "\n"
	
	route = "\toption routers 192.168.1.1;"
	print (route)
	newblock = newblock + route + "\n"

	closeb = "}"
	print (closeb)
	newblock = newblock + closeb + "\n"

	#return (blockname+hwline+fix_addr+route+closeb)
	#return (blockname + "\n" + hwline + "\n" + fix_addr + "\n" + route + "\n" + closeb)
	return (newblock)
	

sysname = "ganesh_laptop"
macaddr = "C0:25:E9:26:81:B2"
ipaddr = "192.168.1.215"

print (ipaddr.split("."))
wlist =  ipaddr.split(".")
print (wlist)

print (str(int(wlist[3])+1))
tstr = (str(int(wlist[3])+1))
print (tstr)

print ("%s.%s.%s.%s" % (wlist[0], wlist[1], wlist[2], tstr))
nip = ("%s.%s.%s.%s" % (wlist[0], wlist[1], wlist[2], tstr))
print (nip)

fline = ("host %s {" % sysname)
print (fline)

sline = ("\thardware ethernet %s;" % macaddr)
print (sline)

exit(1)

print (get_new_dhcp_rule1(sysname, macaddr, nip))
print (get_new_dhcp_rule2(sysname, macaddr, nip))
