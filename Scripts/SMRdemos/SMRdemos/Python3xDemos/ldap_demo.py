'''
LDAP3 demo, based on tutorial on http://ldap3.readthedocs.io/tutorial_intro.html
'''

# first part of demo

from ldap3 import Server, Connection, ALL

server = Server('ipa.demo1.freeipa.org', get_info=ALL)
conn = Connection(server, 'uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org', 'Secret123', auto_bind=True)

#print(server)
#print(server.info)
#print(server.schema)
#print(conn)

print('identity:', conn.extend.standard.who_am_i())

#print(conn)

conn.unbind()

# use with statement to do a simple query

with Connection(server, 'uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org', 'Secret123') as conn:
    conn.search('dc=demo1,dc=freeipa,dc=org', '(&(objectclass=person)(uid=admin))', attributes=['sn', 'krbLastPwdChange', 'objectclass'])
    entry = conn.entries[0]
    print (entry)

