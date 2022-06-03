import ldap3
from ldap3 import Server, Connection


def create_group(server,username,password):
    server = Server(server)
    con = Connection(server, username, password, auto_bind=True)
    groupDN = 'CN=testUSRgroup,OU=testou,DC=metinatakanozel,DC=com'
    objectClass = 'group'
    attr = {
        'cn': 'testUSRgroup',
        'name': 'testUSRgroup',
        'description': 'test grubudur',
        'sAMAccountName': 'testUSRgroup', #windows server 2000 group name
        #'groupType': f'{int(0x00000008)}'#(Distribution Group- universal settings) (default grup type Security Group)     
    }
    con.add(groupDN, objectClass, attr)
    return con.result

serv = '192.168.1.22'
username = 'administrator@metinatakanozel.com'
passw = '1eksi1=0'
#response = create_group(serv,username,passw)
#response = {'result': 0, 'description': 'success', 'dn': '', 'message': '', 'referrals': None, 'type': 'addResponse'}
#response = {'result': 68, 'description': 'entryAlreadyExists', 'dn': '', 'message': '00002071: UpdErr: DSID-030503CF, problem 6005 (ENTRY_EXISTS), data 0\n\x00', 'referrals': None, 'type': 'addResponse'}



