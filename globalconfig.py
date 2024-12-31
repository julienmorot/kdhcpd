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

## Class for global DHCP Configuration

## Dhcpd.conf allow many more options
## In the first we try to do simple
## No one Bootp managing is done

## Some other options will be added later

class globalconfig:
    def __init__(self):
        self.scope = []
        self.static_hosts = []
        
        self.ddns_update_style = "none"
        self.ddns_updates = "off"
        self.authoritative = "true"
        self.log_facility = "local7"
        
        self.domain_name = None
        self.interface_mtu = None
        self.nds_context = None
        self.netbios_node_type = None
        self.nis_domain = None
        self.nisplus_domain = None
        self.nwip_domain = None
        self.nwip_suboptions = None
        self.slp_service_scope = None

        ## Differents values are possibles
        self.routers = None
        self.domain_name_servers = None
        self.cookie_servers = None
        self.finger_server = None
        self.font_servers = None
        self.impress_servers = None
        self.irc_server = None
        self.lpr_servers = None
        self.log_servers = None
        self.mobile_ip_home_agent = None
        self.nds_servers = None
        self.nds_tree_name = None
        self.netbios_dd_server = None
        self.netbios_name_servers = None
        self.nis_servers = None
        self.nisplus_servers = None
        self.nntp_server = None
        self.ntp_servers = None
        self.pop_server = None
        self.resource_location_servers = None
        self.slp_directory_agent = None
        self.smtp_server = None
        self.swap_server = None
        self.tftp_server_name = None
        self.time_servers = None
        self.uap_servers = None
        self.www_server = None
        self.x_display_manager = None
