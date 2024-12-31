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

## Class to manage a key.
## Keys are useful for example with dynamyc DNS updates

## Require in dhcpd.conf :
## ddns-update-style interim;
## ddns-updates on;
## zone foobar.tld. {
##     primary 127.0.0.1;
##     key DHCP_UPDATER;
## }
## 
## zone 1.168.192.in-addr.arpa. {
##     primary 127.0.0.1;
##     key DHCP_UPDATER;
## }

## Syntax of a key in dhcpd.conf :
## key DHCP_UPDATER {
##     algorithm HMAC-MD5;
##     secret pRP5FapFoJ95JEL06sv4PQ==;
## };

## Create a new key : dnskeygen -a HMAC-MD5 -b 128 -n DHCP_UPDATE

class Key:
    def __init__(self):
        self.name = ""
        self.algorithm = "HMAC-MD5"
        self.secret = ""

class Zone:
    def __init__(self):
        self.name = ""
        self.primary = ""
        self.key = ""
