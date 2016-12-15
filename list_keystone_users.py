#import keystoneclient.v2_0.client as ksclient
#from credentials import get_nova_credentials_v2, get_credentials
from mk_legacy_client import make_keystone_client

#credentials = get_nova_credentials_v2()
#print("credentials")
#print(credentials)

#credentials['username'] = 'admin'
#print('new credentials')
#print(credentials)

#credentials2 = get_credentials()
#print("credentials2")
#print(credentials2)

#credentials2['username'] = 'admin'
#print('new credentials2')
#print(credentials2)

try:
    #print("1")
    #keystone = ksclient.Client(**credentials2)
    #print("2")
    #print keystone.auth_url
    cli = make_keystone_client()

    users_list = cli.users.list()
    for u in users_list:
        print "------------------------"
        print u

finally:
    print "Execution Completed."
