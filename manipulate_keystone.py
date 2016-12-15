#from keystoneauth1.identity import v3
#from keystoneauth1 import session
#from keystoneclient.v3 import client
from mk_legacy_client import make_keystone_client

#auth_url = 'http://localhost:5000/v3'
#project_name = 'demo'
#username = 'admin'
#password = 'nomoresecret'
#region_name = 'RegionOne'

#auth = v3.Password( username=username,
#                    password=password,
#                    project_name=project_name,
#                    auth_url=auth_url)

#sess = session.Session(auth=auth)
#keystone = client.Client(session=sess)
#keystone.projects.list()

cli = make_keystone_client()
projects = cli.projects.list()
for p in projects:
    print "--------------------"
    print p

groups = cli.groups.list()
for g in groups:
   print "-----------------------"
   print g

domains = cli.domains.list()
for d in domains:
    print "------------------------"
    print d

roles = cli.roles.list()
for r in roles:
    print "----------------------"
    print r

#tenants = cli.tenants.list()
#for t in tenants:
#    print "------------------------"
#    print t

users = cli.users.list()
for u in users:
    print "------------------------"
    print u

#silvio = cli.users.create(name="Silvio Santos", password="12345", email="silvio.santos@sbt.com.br", enabled=True)

#for u in cli.users.list():
#    print "------------------------"
#    print u

silvio = cli.users.delete(silvio)

cli.users.delete(name="Silvio Santos")
for u in cli.users.list():
    print "------------------------"
    print u
