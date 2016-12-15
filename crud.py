from mk_legacy_client import make_keystone_client

cli = make_keystone_client()

def delete_domain(d_name):
    domain = None
    for d in cli.domains.list():
        if d.name == d_name:
            domain = d

    if domain != None:
        cli.domains.update(domain, enabled=False)
        cli.domains.delete(domain)
        print "Dominio " + d_name + " deletado com sucesso."
    else:
        print "Dominio " + d_name + " nao encontrado."

def get_domain(d_name):
    for d in cli.domains.list():
        if d.name == d_name:
            return d

def delete_group(g_name):
    grp = None
    for g in cli.groups.list():
        if g.name == g_name:
            grp = g

    if grp != None:
        cli.groups.delete(grp)
        print "Grupo " + g_name + " deletado com sucesso."
    else:
        print "Grupo " + g_name + " nao encontrado."   

def get_group(g_name):
    group = None
    for g in cli.groups.list():
        if g.name == g_name:
            return g

def delete_user(u_name):
    user = None
    for u in cli.users.list():
        if u.name == u_name:
            user = u

    if user != None:
        cli.users.delete(user)
        print "Usuario " + u_name + " deletado com sucesso."
    else:
        print "Usuario " + u_name + " nao encontrado."

def get_user(u_name):
    for u in cli.users.list():
        if u.name == u_name:
            return u

def get_role(r_name):
    for r in cli.roles.list():
        if r.name == r_name:
            return r

def get_project(p_name):
    for p in cli.projects.list():
        if p.name == p_name:
            return p
