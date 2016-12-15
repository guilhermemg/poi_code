from mk_legacy_client import make_glance_client

# gera cliente para se conectar com o glance
cli = make_glance_client()

# imprime lista de imagens disponiveis no glance 
images = cli.images.list()
#print(list(images))

for img in images:
    print("--------------------------------------------")
    print(img)
