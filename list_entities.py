import sys
from mk_legacy_client import make_keystone_client

cli = make_keystone_client()

if sys.argv[1] == "users":
    users = cli.users.list()
    for u in users:
        print "------------------------"
        print u

if sys.argv[1] == "projects":
    cli = make_keystone_client()
    projects = cli.projects.list()
    for p in projects:
        print "--------------------"
        print p

if sys.argv[1] == "groups":
    groups = cli.groups.list()
    for g in groups:
        print "-----------------------"
        print g

if sys.argv[1] == "domains":
    domains = cli.domains.list()
    for d in domains:
        print "------------------------"
        print d

if sys.argv[1] == "roles":
    roles = cli.roles.list()
    for r in roles:
        print "----------------------"
        print r

#tenants = cli.tenants.list()
#for t in tenants:
#    print "------------------------"
#    print t

#if sys.argv[1] == "users":
#    users = cli.users.list()
#    for u in users:
#        print "------------------------"
#        print u

#silvio = cli.users.create(name="Silvio Santos", password="12345", email="silvio.santos@sbt.com.br", enabled=True)

#for u in cli.users.list():
#    print "------------------------"
#    print u

#silvio = None
#for u1 in cli.users.list():
#    if u1.name == "Silvio Santos":
#        silvio = u1

#print "Silvio: "
#print str(silvio)

#cli.users.delete(silvio)
#print "Usuario Silvio deletado com sucesso."

#cli.users.delete(name="Silvio Santos")
#for u in cli.users.list():
#    print "------------------------"
#    print u
