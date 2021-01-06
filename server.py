# Simple server holding a RestAPI that implements CRUD operations
# The API is a simplified system to manage data of a store
# The API functions and interactions with the DB are simple
# The ORM implemented is a simplified version of the database
# The objective here is to demonstrate how the tools may work together
# Tools used:
# Python
# Mysql/SQLite (SQL database),
# SQLAlchemy (ORM - object relational mapper),
# Marshmallow (serialize/deserialize objects),
# Flask (server)
# Connexion and Swagger (RestAPI)
import config

conn_app = config.conn_app
conn_app.add_api("swagger.yml")


@conn_app.route("/")
def home():
    return "1"


if __name__ == "__main__":
    conn_app.run(debug=True, host="0.0.0.0")
