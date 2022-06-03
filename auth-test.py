
from ldap3 import Server, Connection

def ldap_Auth(server, username, password): # password control
    server = Server(server)

    con = Connection(server, username, password, auto_bind=False)

    if con.bind() == True:
        print('True')
        return True
    else:
        return {'error':'error'}

serv = '192.168.1.22'
#username = 'metinatakanozel\\Administrator'
#username = 'metinatakanozel\\metin.atakan.ozel'
username = 'administrator@metinatakanozel.com'
passw = '1eksi1=0'

connection = ldap_Auth(serv, username, passw)