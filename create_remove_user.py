from mk_legacy_client import make_keystone_client

cli = make_keystone_client()

silvio = cli.users.create(name="Silvio Santos", password="12345", email="silvio.santos@sbt.com.br", enabled=True)
print "Usuario Silvio criado com sucesso"

cli_silvio = cli.users.get(silvio)
print cli_silvio

#for u in cli.users.list():
#    print "------------------------"
#    print u

#silvio = None
#for u1 in cli.users.list():
#    if u1.name == "Silvio Santos":
#        silvio = u1

#print "Silvio: "
#print str(silvio)

cli.users.delete(cli_silvio)
print "Usuario Silvio deletado com sucesso."

print "Lista usuarios ------------------------------------------------"
for u in cli.users.list():
    print "------------------------"
    print u

