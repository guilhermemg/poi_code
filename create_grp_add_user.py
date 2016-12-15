from mk_legacy_client import make_keystone_client
from crud import delete_domain, delete_group, delete_user

cli = make_keystone_client()

delete_domain("SBT")
delete_group("Usuarios SBT")
delete_user("Silvio Santos")


domainSBT = cli.domains.create(name="SBT", description="Dominio SBT", enabled=True)
print "Domain SBT criado com sucesso"
print domainSBT
print "-----------"

group1 = cli.groups.create(name="Usuarios SBT", description="Usuarios SBT", domain=domainSBT)
print "Grupo criado com sucesso"
print group1
print "-----------"

silvio = cli.users.create(name="Silvio Santos", description="Dono do SBT", password="12345", email="silvio.santos@sbt.com.br", enabled=True)
print "Usuario Silvio criado com sucesso"
print silvio
print "-----------"

print "Lista usuarios ------------------------------------------------"
for u in cli.users.list():
    print "------------------------"
    print u

cli.users.add_to_group(silvio, group1)
print "Usuario Silvio adicionado a Grupo SBT"

for g in cli.groups.list():
    print "======================"
    print g

