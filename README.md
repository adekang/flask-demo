```bash
blinker==1.7.0
certifi==2023.11.17
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
docopt==0.6.2
Flask==3.0.0
idna==3.6
importlib-metadata==7.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
pip==23.0.1
pipreqs==0.4.13
requests==2.31.0
setuptools==58.1.0
urllib3==2.1.0
Werkzeug==3.0.1
yarg==0.1.9
zipp==3.17.0
```


# 数据库字段更新
```bash
# 第一次创建项目初始化时使用
flask db init 
# 后面每次修改数据库字段时使用
flask db migrate
flask db upgrade
```
# 目录层级

```bash
├── .venv/
├── app/
│   └── api/ # api 接口模块
│       └── __init__.py # 注册以及生成蓝图
│       └── common/ # 公共方法
│       └── models/ # 模型
│       └── resources/ # 接口
│       └── schema/ # 校验
│   └── __init__.py # 整个应用的初始化
│   └── config.py # 配置项
│   └── manage.py # 数据库迁移工具管理
├── .env # 环境变量
├── run.py # 入口文件
```