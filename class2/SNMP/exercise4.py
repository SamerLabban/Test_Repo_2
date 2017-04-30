from snmp_helper import snmp_get_oid,snmp_extract

def output_Name_Descr(IP, COMMUNITY_STRING, SNMP_PORT, OID):
    a_device = (IP, COMMUNITY_STRING, SNMP_PORT)
    snmp_data = snmp_get_oid(a_device, oid=OID, display_errors=True)
    output = snmp_extract(snmp_data)
    return output

def main():

    COMMUNITY_STRING = 'galileo'
    SNMP_PORT = 161
    IP_rtr1 = '184.105.247.70'
    IP_rtr2 = '184.105.247.71'
    sysName_OID = '1.3.6.1.2.1.1.5.0'
    sysDescr_OID = '1.3.6.1.2.1.1.1.0'

    rtr1_Name = output_Name_Descr(IP_rtr1, COMMUNITY_STRING, SNMP_PORT, sysName_OID)
    rtr1_Descr = output_Name_Descr(IP_rtr1, COMMUNITY_STRING, SNMP_PORT, sysDescr_OID)

    rtr2_Name = output_Name_Descr(IP_rtr2, COMMUNITY_STRING, SNMP_PORT, sysName_OID)
    rtr2_Descr = output_Name_Descr(IP_rtr2, COMMUNITY_STRING, SNMP_PORT, sysDescr_OID)

    print "pynet-rtr1: \nName: %s \nDescription: %s" % (rtr1_Name, rtr1_Descr)
    print "pynet-rtr2: \nName: %s \nDescription: %s" % (rtr2_Name, rtr2_Descr)

if __name__ == "__main__":
	main()
