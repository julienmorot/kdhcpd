## Copyright (C) 2005, Julien Morot
## KDHCPD, a GUI to manage your DHCP Server

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

## This is classes for every permitted option
## Every class are a subclassed object of QListViewItem
## This is defined because each object if inserted into the user-selected QListView
##
## Each class as the same caracteritics :
## They have for parent the QListView
## relative to the dhcp.conf object they defined (host, pool, group, subnet)
## Then they every have 4 attributes :
## - The value of the option
## - A label describing shortly the option
## - A type used to help the user input and optionnaly the developper
## - A description used to help the user input and optionnaly the developper
##
## The only thing which differ between theses classes
## is that some options could have different arguments,
## like the list of dns name servers so a string or a list is used

from qt import *

class subnet:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "IP Address"
        self.description = "Address of the network segment."

class netmask:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "IP Address"
        self.description = "Address of the network segment."

class rangebegining:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "IP Address"
        self.description = "First allowable IP address."

class rangeend:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "IP Address"
        self.description = "Last allowable IP address."

class broadcast_address:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "IP Address"
        self.description = "Broadcast address of the network segment."

class domain_name:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "String"
        self.description = ""

class interface_mtu:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "Integer"
        self.description = ""

class nds_context:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "String"
        self.description = ""

class netbios_node_type:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "Integer"
        self.description = ""

class nis_domain:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "String"
        self.description = ""

class nisplus_domain:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "String"
        self.description = ""

class nwip_domain:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "String"
        self.description = ""

class nwip_suboptions:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "String"
        self.description = ""

class slp_service_scope:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "Boolean Text"
        self.description = ""

class interface_mtu:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "Integer"
        self.description = ""

class nds_tree_name:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "String"
        self.description = ""

class all_subnets_local:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "Boolean"
        self.description = ""

class max_lease_time:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "Seconds"
        self.description = ""

class default_lease_time:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "Seconds"
        self.description = ""

class routers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class domain_name_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class cookie_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class finger_server:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class font_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class impress_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class irc_server:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class lpr_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class log_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class nds_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class netbios_dd_server:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class netbios_name_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class nis_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class nisplus_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class nntp_server:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class ntp_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class pop_server:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class resource_location_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class slp_directory_agent:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class smtp_server:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class swap_server:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class tftp_server_name:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class time_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class time_servers:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

class x__display_manager:
    def __init__(self):
        self.value = []
        self.label = ""
        self.type = "IP Address"
        self.description = ""

## Not used options

##arp-cache-timeout
##bootfile-name
##boot-size
##default-ip-ttl
##default-tcp-ttl
##dhcp-client-identifier
##dhcp-max-message-size
##dhcp-parameter-request-list
##extensions-path
##host-name
##ieee802-3-encapsulation
##ip-forwarding
##mask-supplier
##max-dgram-reassembly
##merit-dump
##netbios-scope
##non-local-source-routing
##path-mtu-aging-timeout
##path-mtu-plateau-table
##perform-mask-discovery
##policy-filter
##root-path
##router-discovery
##router-solicitation-address
##static-routes
##subnet-mask
##subnet-selection
##tcp-keepalive-garbage
##tcp-keepalive-interval
##time-offset
##trailer-encapsulation
##user-class
##vendor-class-identifier
##vendor-encapsulated-options
##self.ien116-name-servers
##streettalk-directory-assistance-server
##streettalk-server
##uap-servers
##self.mobile-ip-home-agent

## Not user configurable so it will never be used

##dhcp-lease-time
##dhcp-message
##dhcp-message-type
##dhcp-option-overload
##dhcp-rebinding-time
##dhcp-renewal-time
##dhcp-requested-address
##dhcp-server-identifier


