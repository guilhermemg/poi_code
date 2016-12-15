from mk_legacy_client import make_keystone_client
from crud import get_role, get_user, get_project, get_domain

cli = make_keystone_client()

admin_role = get_role("admin")
silvio = get_user("Silvio Santos")
sbt_domain = get_domain("Dominio SBT")
demo_project = get_project("demo")

silvio_demo_role = cli.roles.grant(role=admin_role, user=silvio, project=demo_project)
print "Role admin granted to Usuario Silvio em Projeto demo"

