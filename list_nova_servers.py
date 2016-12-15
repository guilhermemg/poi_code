#from credentials import get_nova_credentials_v2
from novaclient.client import Client
from mk_legacy_client import make_legacy_client

#credentials = get_nova_credentials_v2()
#print(credentials)

#nova_client = Client(**credentials)
cli = make_legacy_client()

srvs = cli.servers
srvs

print(srvs.list())
