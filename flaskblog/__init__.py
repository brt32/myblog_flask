from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '64fdee2e556b7733d9f24f198e3137e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
app.config['TESTING'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LdXcbEZAAAAAFKtQNNEULYCeahvf2_ApW6lEhkG'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LdXcbEZAAAAAFXPr6bRO1A_THkrLKlj7zq9cuZe'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes