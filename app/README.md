from app import db, create_app

db.create_all(app=create_app())

在MAC上安装mysql并与sqlalchemy关联

```
pipenv install mysqlclient

```
出现报错. 

```
OSError: mysql_config not found
```
查看```echo $PATH```发现mysql不在路径下，使用以下命令添加路径：

```
export MYSQL_HOME=/usr/local/mysql/bin
export PATH=$PATH:$MYSQL_HOME
```
又出现mysql包不能导入错误
```
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/:$DYLD_LIBRARY_PATH
```
  
  
将db创造为全局变量（需要在其他模块中导入使用），在初始化app后，使用db.init_app(app)将其初始化。  

```
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
# create the db object before app object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mys3326999@localhost/test'
    app.config['SECRET_KEY'] = 'mysecret'
    # create the db first and init the app with the db beforehand later
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app
```

使用以下命令在终端进入进入python，并使用```db.create_all(app)```将创建表

```
from app import db, create_app
db.create_all(app=create_app())
```