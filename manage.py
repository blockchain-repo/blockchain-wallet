import config
from app import app

config.create_config()
config.set_config()
app.debug = True
app.run(host='0.0.0.0')
