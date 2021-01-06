import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))


# Connexion application instance
conn_app = connexion.App(__name__, specification_dir=basedir)

# Get flask app instance
app = conn_app.app

# SQLite URL and Mysql URL for SQLAlchemy
sqlite_url = "sqlite:///" + os.path.join(basedir, "simplestore.db")
mysql_url = "mysql+pymysql://root:YOUR USER HERE@localhost/simplestore"

# SQLAlchemy configuration
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = mysql_url
app.config["SQlALCHEMY_TRACK_MODIFICATIONS"] = False

# SQLAlchemy DB and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)
