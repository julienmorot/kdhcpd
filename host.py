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

## Class for a DHCP Host

from qt import *

class host(QListViewItem):
    def __init__(self, listview):
        QListViewItem.__init__(self, listview)
##        self.allowedoptions = ["name", "hardware", "fixed-address", "domain-name", "interface-mtu", "nds-context", "netbios-node-type", "nis-domain", "nisplus-domain", "nwip-domain", "nwip-suboptions", "slp-service-scope" \
##            "routers", "domain-name-servers", "finger-server", "font-servers", "impress-servers", \
##            "irc-server", "log-servers", "mobile-ip-home-agent", \
##            "nds-servers", "nds-tree-name", "netbios-dd-server", "netbios-name-servers", "nis-servers", \
##            "nisplus-servers", "nntp-server", "ntp-servers", "pop-server", "resource-location-servers", \
##            "slp-directory-agent", "smtp-server", "swap-server", "tftp-server-name", "time-servers", "uap-servers" \
##            "www-server", "x-display-manager"]
        self.hostname = None
        self.hardware_ethernet = None
##        The address could be an IP address or a resolvable FQDN
        self.fixed_address = None


class hostname:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "String"
        self.description = "Hostname for the static host."

class hardware_ethernet:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "MAC Address"
        self.description = "MAC Address of the network interface."

class fixed_address:
    def __init__(self):
        self.value = ""
        self.label = ""
        self.type = "IP Address or FQDN"
        self.description = "Static IP address to allow. If you specify a FQDN, it should be resolvable."

