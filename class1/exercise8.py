from ciscoconfparse import CiscoConfParse

#open the cisco file and store it in a variable
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

#search for any line in our confparse object (cisco_cfg) that begins with the word "crypto map CRYPTO"
intf = cisco_cfg.find_objects(r"^crypto map CRYPTO")

#print type(intf)

#Get all children (children and grandchildren) elements
for i in intf:
    print i
    for child in i.all_children:    
        print child.text
    print "\n"


