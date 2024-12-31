import string
from globalconfig import *
import re

from options import *
from scope import *
from host import *
from key import *
from group import *
from pool import *

class dhcpBackend:
    def __init__(self, listStruc):
        self.conf = []
        self.cleanedfile = []
        self.linenum = 0
        
        dhcpdconf = globalconfig()
        
        self.cleanfile()
        self.parsefile(listStruc)
    
## Open the file put off comments and empty lines
    def cleanfile(self):
        try:
            fd = open('./dhcpd.conf', 'r')
            lines = fd.readlines()
            fd.close ()
        except IOError:
            lines = []

        for line in lines:
            if line[0] == '#' or line == "\n":
                continue
            else:
                strippedline = string.strip(line)
                self.cleanedfile.append(strippedline)

    def parsefile(self, ListDhcpStruct):
        print "-------------------------------------------------"
        numberoflines = len(self.cleanedfile)
        self.linenum = 0
        while self.linenum != numberoflines:
            
##
##  Now, I'll try to play with python regexp to parse dhcpd.conf
##
            if re.match("^host", self.cleanedfile[self.linenum]):
                print self.cleanedfile[self.linenum], "Hey! here there's a host!"
                statichost = host(ListDhcpStruct)
                self.parseHostOptions(statichost)
##                 self.dhcpdconf.static_hosts.append(statichost)
                
            if re.match("^key", self.cleanedfile[self.linenum]):
                print "It's secret! a Key definition!"
                print "Now I think we can create a loop which will end with char }"
            
            if re.match("^zone", self.cleanedfile[self.linenum]):
                print "Beautiful! You're the king of the weurld becoz there's a dns zone definition!"

            if re.match("^subnet", self.cleanedfile[self.linenum]):
                dhcpsubnet = scope(ListDhcpStruct)
                self.parseSubnetOptions(dhcpsubnet)

## Wrong position here but it's temporary...
##                print self.cleanedfile[linenum], "How my god! A subnet definition! I'm so happy!"
##                print "Now I think we can create a loop which will end with char }"
                
##                if re.match("^group", self.cleanedfile[self.linenum]):
##                    print self.cleanedfile[self.linenum], "Wow! It's christmas! Now I look a group definition!"
##                    print "Now I think we can create a loop which will end with char }"
                
##                if re.match("^pool", self.cleanedfile[self.linenum]):
##                    print self.cleanedfile[self.linenum], "Jinggle bells! A pool definition!"
##                    print "Now I think we can create a loop which will end with char }"
            self.linenum = self.linenum + 1

## Done!
    def parseHostOptions(self, hostobject):
        splittedline = string.split(self.cleanedfile[self.linenum], " ")
        hostobject.hostname = hostname()
        hostobject.hostname.value = splittedline[1]
        while self.cleanedfile[self.linenum] != "}":
            opt = string.split(self.cleanedfile[self.linenum], " ")
            if opt[0] == "hardware":
                hostobject.hardware_ethernet = hardware_ethernet()
                hostobject.hardware_ethernet.value = string.strip(opt[2], ";")
            elif opt[0] == "fixed-address":
                hostobject.fixed_address = fixed_address()
                hostobject.fixed_address.value = string.strip(opt[1], ";")
            self.linenum = self.linenum + 1

## To refactor
    def parseKeyOptions(self, keyobject):
        splittedline = string.split(self.cleanedfile[self.linenum], " ")
        keyobject.name = splittedline[1]
        self.linenum = self.linenum + 1
        while self.cleanedfile[self.linenum] != "}":
            opt = string.split(self.cleanedfile[self.linenum], " ")
            if opt[0] == "secret":
                keyobject.secret = opt[1]
            self.linenum = self.linenum + 1

## To refactor according to the refactored parseKeyOptions()
    def parseZoneOptions(self, zoneobject):
        splittedline = string.split(self.cleanedfile[self.linenum], " ")
        zoneobject.name = splittedline[1]
        self.linenum = self.linenum + 1
        while self.cleanedfile[self.linenum] != "}":
            opt = string.split(self.cleanedfile[self.linenum], " ")
            if opt[0] == "primary":
                zoneobject.primary = opt[1]
            elif opt[0] == "key":
                zoneobject.key = opt[1]
            self.linenum = self.linenum + 1

    def parseSubnetOptions(self, subnetobject):
        splittedline = string.split(self.cleanedfile[self.linenum], " ")
        subnetobject.subnet = subnet()
        subnetobject.subnet.value = splittedline[1]
        subnetobject.netmask = netmask()
        subnetobject.netmask.value = splittedline[3]
        self.linenum = self.linenum + 1
        
        while self.cleanedfile[self.linenum] != "}":
            opt = string.split(self.cleanedfile[self.linenum], " ")
            if opt[0] == "range":
                subnetobject.rangebegining = rangebegining()
                subnetobject.rangebegining.value = string.split(opt[1], " ")
                subnetobject.rangeend = rangeend()
                subnetobject.rangeend.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "broadcast-address":
                subnetobject.broadcast_address = broadcast_address()
                subnetobject.broadcast_address.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "domain-name":
                subnetobject.domain_name = domain_name()
                subnetobject.domain_name.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "interface-mtu":
                subnetobject.interface_mtu = interface_mtu()
                subnetobject.interface_mtu.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "nds-context":
                subnetobject.nds_context = nds_context()
                subnetobject.nds_context.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "netbios-node-type":
                subnetobject.netbios_node_type = netbios_node_type()
                subnetobject.netbios_node_type.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "nis-domain":
                subnetobject.nis_domain = nis_domain()
                subnetobject.nis_domain.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "nisplus-domain":
                subnetobject.nisplus_domain = nisplus_domain()
                subnetobject.nisplus_domain.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "nwip-domain":
                subnetobject.nwip_domain = nwip_domain()
                subnetobject.nwip_domain.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "nwip-suboptions":
                subnetobject.nwip_suboptions = nwip_suboptions()
                subnetobject.nwip_suboptions.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "slp-service-scope":
                subnetobject.slp_service_scope = slp_service_scope()
                subnetobject.slp_service_scope.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "all-subnets-local":
                subnetobject.all_subnets_local = all_subnets_local()
                subnetobject.all_subnets_local.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "default-lease-time":
                subnetobject.default_lease_time = default_lease_time()
                subnetobject.default_lease_time.value = string.split(opt[2], " ")
            elif opt[0] == "option" and opt[1] == "max-lease-time":
                subnetobject.max_lease_time = max_lease_time()
                subnetobject.max_lease_time.value = string.split(opt[2], " ")
            
            elif opt[0] == "option" and opt[1] == "routers":
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.routers = routers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.routers.value.append(tmp[0])
                    print subnetobject.routers.value
                    i = i + 1
                subnetobject.routers.value.reverse()                
            elif opt[0] == "option" and opt[1] == domain-name-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.domain_name_servers = domain_name_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.domain_name_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.domain_name_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == cookie-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.cookie_servers = cookie_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.cookie_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.cookie_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == finger-server:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.finger_server = finger_server()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.finger_server.value.append(tmp[0])
                    i = i + 1
                subnetobject.finger_server.value.reverse()
            elif opt[0] == "option" and opt[1] == font-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.font_servers = font_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.font_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.font_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == impress-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.impress_servers = impress_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.impress_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.impress_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == irc-server:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.irc_server = irc_server()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.irc_server.value.append(tmp[0])
                    i = i + 1
                subnetobject.irc_server.value.reverse()
            elif opt[0] == "option" and opt[1] == lpr-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.lpr_servers = lpr_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.lpr_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.lpr_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == log-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.log_servers = log_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.log_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.log_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == mobile-ip-home-agent:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.mobile_ip_home_agent = mobile_ip_home_agent()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.mobile_ip_home_agent.value.append(tmp[0])
                    i = i + 1
                subnetobject.mobile_ip_home_agent.value.reverse()
            elif opt[0] == "option" and opt[1] == nds-tree-name:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.nds_tree_name = nds_tree_name()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.nds_tree_name.value.append(tmp[0])
                    i = i + 1
                subnetobject.nds_tree_name.value.reverse()
            elif opt[0] == "option" and opt[1] == netbios-dd-server:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.netbios_dd_server = netbios_dd_server()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.netbios_dd_server.value.append(tmp[0])
                    i = i + 1
                subnetobject.netbios_dd_server.value.reverse()
            elif opt[0] == "option" and opt[1] == netbios-name-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.netbios_name_servers = netbios_name_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.netbios_name_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.netbios_name_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == nis-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.nis_servers = nis_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.nis_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.nis_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == nisplus-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.nisplus_servers = nisplus_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.nisplus_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.nisplus_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == nntp-server:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.nntp_server = nntp_server()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.nntp_server.value.append(tmp[0])
                    i = i + 1
                subnetobject.nntp_server.value.reverse()
            elif opt[0] == "option" and opt[1] == ntp-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.ntp_servers = ntp_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.ntp_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.ntp_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == pop-server:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.pop_server = pop_server()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.pop_server.value.append(tmp[0])
                    i = i + 1
                subnetobject.pop_server.value.reverse()
            elif opt[0] == "option" and opt[1] == resource-location-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.resource_location_servers = resource_location_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.resource_location_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.resource_location_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == slp-directory-agent:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.slp_directory_agent = slp_directory_agent()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.slp_directory_agent.value.append(tmp[0])
                    i = i + 1
                subnetobject.slp_directory_agent.value.reverse()
            elif opt[0] == "option" and opt[1] == smtp-server:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.smtp_server = smtp_server()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.smtp_server.value.append(tmp[0])
                    i = i + 1
                subnetobject.smtp_server.value.reverse()
            elif opt[0] == "option" and opt[1] == swap-server:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.swap_server = swap_server()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.swap_server.value.append(tmp[0])
                    i = i + 1
                subnetobject.swap_server.value.reverse()
            elif opt[0] == "option" and opt[1] == tftp-server-name:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.tftp_server_name = tftp_server_name()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.tftp_server_name.value.append(tmp[0])
                    i = i + 1
                subnetobject.tftp_server_name.value.reverse()
            elif opt[0] == "option" and opt[1] == time-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.time_servers = time_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.time_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.time_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == uap-servers:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.uap_servers = uap_servers()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.uap_servers.value.append(tmp[0])
                    i = i + 1
                subnetobject.uap_servers.value.reverse()
            elif opt[0] == "option" and opt[1] == www-server:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.www_server = www_server()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.www_server.value.append(tmp[0])
                    i = i + 1
                subnetobject.www_server.value.reverse()
            elif opt[0] == "option" and opt[1] == x-display-manager:
                i = 0
                paramnumber = len(opt)
                optnumber = paramnumber - 2
                opt.reverse()
                subnetobject.x_display_manager = x_display_manager()
                while (i != optnumber):
                    tmp = string.split(opt[i], ";")
                    subnetobject.x_display_manager.value.append(tmp[0])
                    i = i + 1
                subnetobject.x_display_manager.value.reverse()
            
            self.linenum = self.linenum + 1
    
## TODO : write :
##def parsePoolOptions()
##def parseGroupOptions()
##def parseGlobalOptions()
