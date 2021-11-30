from flask import Flask
import psycopg2
import os

HOST = "localhost"
PORT = "55432"
DATABASE = "my_database"
USER_MASTER = "user1"
PASSWORD_MASTER = "password1"
USER_SLAVE = "user2"
PASSWORD_SLAVE = "password2"


app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<p>PID:" + str(os.getpid()) + "</p>"




if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
