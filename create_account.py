"""The role of this module is to create an account and write to the '.account' file

"""

from bigchaindb_driver.crypto import generate_keypair
import rapidjson

def create_account(username):
    keypair = generate_keypair()

    account = {
        'verifying_key' : keypair.verifying_key ,
        'signing_key' : keypair.signing_key ,
        'username' : username
    }


    f = open('.account','w')
    json_account = rapidjson.dumps(account)
    f.write(json_account)
    f.close()
    return(account)

if __name__=='__main__':
    username = input ('Pick a username:\n')
    print(create_account(username))
    
