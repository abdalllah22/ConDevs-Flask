from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)


app.config['SECRET_KEY'] = 'Secret'

### DATABASE SETUP ##########
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zxzx1212@localhost/condevs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

### LOGIN CONFIGS ##########
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


### Register apps ##########
from dev_blog.core.views import core
from dev_blog.error_pages.handlers import error_pages
from dev_blog.users.views import users
from dev_blog.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
