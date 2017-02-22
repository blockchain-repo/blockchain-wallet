import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from create_account import create_account

print(create_account('cindy'))
