"""The role of this module is to create the config and write to the '.config' file

"""
import json
import os
import sys

def create_config(host_ip='127.0.0.1',host_port='9984'):

    config = {
        'host_ip' : host_ip,
        'host_port' : host_port
    }

    f = open('.config','w')
    json_config = json.dumps(config)
    f.write(json_config)
    f.close()
    return(config)

if __name__=='__main__':
    isConfigExist = os.path.exists('.config')
    if isConfigExist:
        print("this client already exists an config.")
        sys.exit()
    if len(sys.argv)==1:
        c = create_config()
    elif len(sys.argv)==2:
        host_ip = sys.argv[1]
        c= create_config(host_ip)
    elif len(sys.argv)==3:
        host_ip = sys.argv[1]
        host_port = sys.argv[2]
        c= create_config(host_ip,host_port)
    else:
        print("Please provide parameters of `ip(default 127.0.0.1)` `port(default 9984)`")
        sys.exit()
    print(json.dumps(c,indent=4))
