import os
from flask import Flask
from .config import config
from .api.models import db
from .api import api_blueprint
from .manage import migrate
# *important 所有数据库模型 需要显式的在这里导入
from .api.models.users import UserModel
from flask_cors import CORS


def create_app(config_name):
    # 初始化 Flask 项目
    app = Flask(__name__)
    # 解决跨域问题
    CORS(app)
    # 加载配置项
    app.config.from_object(config[config_name])
    # 初始化数据库ORM
    db.init_app(app)
    # 初始化数据库ORM迁移插件
    migrate.init_app(app, db)
    # 注册蓝图
    app.register_blueprint(api_blueprint)
    return app


app = create_app(os.getenv('FLASK_ENV', 'development'))
