
import json
from ldap3 import SUBTREE, Server, Connection
import ldap3
def get_domainusers_type_user(server, username, password):  # tüm userler getirilir 5000 sınırı olabilir !!!! 6684 kayıt getirdi 5000 sınırı olmayabilir
    server = Server(server)
    con = Connection(server, username, password, auto_bind=True, auto_range=True,)
    result = con.extend.standard.paged_search(search_base='DC=metinatakanozel,DC=com',
                                              search_filter='(&(objectCategory=user)(objectClass=user))',
                                              attributes=['objectGUID','sAMAccountName','userAccountControl'],
                                              size_limit=25,
                                              generator=True)
    # 1000 in üzerinde kayıt almak için "con.extend.standard.paged_search" kullanıldı
    response_list = []
    for x in result:# attributesiz gelenler var
        if 'attributes' in x:
            #print(x['attributes']['objectGUID'],' ',x['attributes']['sAMAccountName'])
            resp_model = {}
            resp_model['objectGUID'] = x['attributes']['objectGUID'][1:-1]
            resp_model['userLogonName'] = x['attributes']['sAMAccountName']
            resp_model['userAccountStatus'] = x['attributes']['userAccountControl']
            response_list.append(resp_model)
            resp_model = {}

    
    return response_list

serv = '192.168.1.22'
username = 'administrator@metinatakanozel.com'
passw = '1eksi1=0'
#response = get_domainusers_type_user(serv, username, passw)
response = [
    {'objectGUID': 'e600d8d8-307f-48d1-b12f-10f2955be364', 'userLogonName': 'test.user.two', 'userAccountStatus': 66048},
    {'objectGUID': 'f5cc4648-c126-4860-807c-fe788bc15762', 'userLogonName': 'test.user.one', 'userAccountStatus': 66048},
    {'objectGUID': 'ef7710b1-e7f6-4cd1-8c2d-703e1d5252fd', 'userLogonName': 'metin.atakan.ozel', 'userAccountStatus': 66048},
    {'objectGUID': '70984aa3-d12b-4211-9cd1-dc7e4b593d2d', 'userLogonName': 'krbtgt', 'userAccountStatus': 514},
    {'objectGUID': '5142e245-2ec1-4ccf-8194-91177a4ae689', 'userLogonName': 'Guest', 'userAccountStatus': 66082},
    {'objectGUID': '3008cae8-0aac-49e7-99fc-3254fbec0168', 'userLogonName': 'Administrator', 'userAccountStatus': 66048}
]

def get_user_with_all_attributes_by_GUID(server, username, password, guid):
    server = Server(server)

    con = Connection(server, username, password, auto_bind=True)

    con.search(search_base='DC=metinatakanozel,DC=com',search_scope=SUBTREE,
               search_filter=f'(&(objectCategory=user)(objectClass=user)(objectGUID={guid}))',
               attributes=[ldap3.ALL_ATTRIBUTES, ldap3.ALL_OPERATIONAL_ATTRIBUTES])
    user_info = json.loads(con.response_to_json())['entries']

    print(user_info)

#user_response = get_user_with_all_attributes_by_GUID(serv, username, passw, "ef7710b1-e7f6-4cd1-8c2d-703e1d5252fd")
user_response = [{'attributes': 
    {'accountExpires': '9999-12-31 23:59:59.999999+00:00', 
    'adminCount': 1, 
    'badPasswordTime': '2022-04-05 11:29:35.092936+00:00', 
    'badPwdCount': 0, 
    'cn': 'metin atakan özel', 
    'codePage': 0, 
    'countryCode': 0, 
    'dSCorePropagationData': ['2022-04-05 10:07:11+00:00', '1601-01-01 00:00:00+00:00'], 
    'displayName': 'metin atakan özel', 
    'distinguishedName': 'CN=metin atakan özel,OU=testou,DC=metinatakanozel,DC=com', 
    'givenName': 'metin atakan', 
    'instanceType': 4, 
    'lastLogoff': '1601-01-01 00:00:00+00:00', 
    'lastLogon': '2022-04-05 11:29:55.952200+00:00', 
    'lastLogonTimestamp': '2022-04-05 09:45:48.091799+00:00', 
    'logonCount': 3, 
    'name': 'metin atakan özel', 
    'objectCategory': 'CN=Person,CN=Schema,CN=Configuration,DC=metinatakanozel,DC=com', 
    'objectClass': ['top', 'person', 'organizationalPerson', 'user'], 
    'objectGUID': '{ef7710b1-e7f6-4cd1-8c2d-703e1d5252fd}', 
    'objectSid': 'S-1-5-21-1910307614-1461413344-2550438435-1106', 
    'primaryGroupID': 513, 
    'pwdLastSet': '2022-04-05 09:45:01.747906+00:00', 
    'sAMAccountName': 'metin.atakan.ozel', 
    'sAMAccountType': 805306368, 
    'sn': 'özel', 
    'uSNChanged': 16407, 
    'uSNCreated': 12802, 
    'userAccountControl': 66048, 
    'userPrincipalName': 'metin.atakan.ozel@metinatakanozel.com', 
    'whenChanged': '2022-04-05 10:07:11+00:00', 
    'whenCreated': '2022-04-05 09:45:01+00:00'}, 
    'dn': 'CN=metin atakan özel,OU=testou,DC=metinatakanozel,DC=com'}
]



def create_user(server,username,password):
    server = Server(server)
    con = Connection(server, username, password, auto_bind=True)
    userDN = 'CN=testUSRadd1,OU=testou,DC=metinatakanozel,DC=com'
    objectClass = 'user'
    attr = {
        'cn': 'testUSRadd1',
        'name': 'testUSRadd1',
        'description': 'testUSRadd1',
        'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
        'sAMAccountName': 'testUSRad1d',
        'userPrincipalName': 'metin.atakan.ozel@metinatakanozel.com'
        
    }
    con.add(userDN, objectClass, attr) #before create a user
    print(con.result)
    ################ you must have ssl cert for password set and enable user #######################
    ################ you must have Active Directory Certificate Services in DC (https://www.youtube.com/watch?v=JFPa_uY8NhY) #######################
    userPswd = "1eksi1=00"
    con.extend.microsoft.modify_password(userDN, userPswd) #after set password 
    con.modify(userDN, {'userAccountControl': [('MODIFY_REPLACE', 512)]}) # and then set enable user
    #con.modify(userDN, {'userAccountControl': [('MODIFY_REPLACE', 2)]}) # for disable
    
    return con.result

serv = 'ldaps://192.168.1.21:636'
username = 'administrator@metinatakanozel.com'
passw = '1eksi1=0'
response = create_user(serv,username,passw)