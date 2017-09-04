import config

config.create_config()
config.set_config()

from app import app

debug = config.config['app']['debug']
host = config.config['app']['host']
port = config.config['app']['port']
app.debug = debug
app.run(host=host, port=port)
