from flask import Flask

app = Flask(__name__)  # 创建Flask application对象

from app.views import views
