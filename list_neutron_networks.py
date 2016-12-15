#!/usr/bin/env python

from mk_legacy_client import make_neutron_client

cli = make_neutron_client()
netw = cli.list_networks()

netws = netw['networks']
for n in netws:
    print "------------------------------------------------------"
    print n
