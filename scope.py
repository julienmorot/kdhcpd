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

## Class for a subnet

## Dhcpd.conf allow many more options
## In the first we try to do simple

from qt import *

class scope(QListViewItem):
    def __init__(self, listview):
        QListViewItem.__init__(self, listview)
        self.subnet = None
        self.netmask = None
        self.rangebegining = None
        self.rangeend = None
        
        self.max_lease_time = 25200
        self.default_lease_time = 25200
        
        self.broadcast_address = None
        self.domain_name = None
        self.interface_mtu = None
        self.nds_context = None
        self.netbios_node_type = None
        self.nis_domain = None
        self.nisplus_domain = None
        self.nwip_domain = None
        self.nwip_suboptions = None
        self.slp_service_scope = None
        self.all_subnets_local = None

        ## Differents values are possibles
        self.routers = []
        self.domain_name_servers = []
        self.cookie_servers = []
        self.finger_server = []
        self.font_servers = []
        self.impress_servers = []
        self.irc_server = []
        self.lpr_servers = []
        self.log_servers = []
        self.mobile_ip_home_agent = []
        self.nds_servers = []
        self.nds_tree_name = []
        self.netbios_dd_server = []
        self.netbios_name_servers = []
        self.nis_servers = []
        self.nisplus_servers = []
        self.nntp_server = []
        self.ntp_servers = []
        self.pop_server = []
        self.resource_location_servers = []
        self.slp_directory_agent = []
        self.smtp_server = []
        self.swap_server = []
        self.tftp_server_name = []
        self.time_servers = []
        self.uap_servers = []
        self.www_server = []
        self.x_display_manager = []
