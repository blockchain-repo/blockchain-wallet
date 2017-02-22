from bigchaindb_driver.crypto import generate_keypair
import rapidjson

keypair = generate_keypair()
username = input ('Pick a username:\n')

account = {
    'verifying_key' : keypair.verifying_key ,
    'signing_key' : keypair.signing_key ,
    'username' : username
}

print (account)

f = open('.account','w')
json_account = rapidjson.dumps(account)
f.write(json_account)
f.close()
