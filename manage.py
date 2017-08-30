import config

config.create_config()
config.set_config()

from app import app

app.debug = True
app.run(host='0.0.0.0', port=5000)
