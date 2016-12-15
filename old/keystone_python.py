#!/bin/python

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

auth = v3.Password(auth_url='http://localhost:5000/v3',
	 	    username='admin',
                    password='nomoresecret',
                    project_id='demo')
sess = session.Session(auth=auth)
ks = client.Client(session=sess)
users = ks.users.list()
print(users)
