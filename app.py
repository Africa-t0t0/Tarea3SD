from flask import Flask, request
import psycopg2
import os

HOST = "localhost"
PORT_MASTER = "55432"
PORT_SLAVE = "65432"
DATABASE = "my_database"
USER_MASTER = "user1"
PASSWORD_MASTER = "password1"
USER_SLAVE = "user2"
PASSWORD_SLAVE = "password2"


app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<p>PID:" + str(os.getpid()) + "</p>"

@app.route("/addproduct", methods=["POST"])
def addproduct():
    # Connect to master
    conn = psycopg2.connect(host=HOST,
                            port=PORT_MASTER,
                            database=DATABASE,
                            user=USER_MASTER,
                            password=PASSWORD_MASTER)

    # Get cursor
    cur = conn.cursor()
    # Execute query
    name = request.form.get("name")
    value = request.form.get("value")

    cur.execute("INSERT INTO products (name, value) VALUES (%s, %s)",
                (name, value))

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()
    return "<p>Product added</p>"


@app.route("/getproducts/<product>", methods=["GET"])
def getproducts(product):
    # Connect to slave
    product = product+"%"
    print(product)
    conn = psycopg2.connect(host=HOST,
                            port=PORT_SLAVE,
                            database=DATABASE,
                            user=USER_SLAVE,
                            password=PASSWORD_SLAVE)

    # Get cursor
    cur = conn.cursor()

    query = ("SELECT name FROM products WHERE name LIKE %s")
    # Execute query
    cur.execute(query, (product,))

    # Fetch all rows
    rows = cur.fetchall()
    print(rows)
    # Close connection
    conn.close()
    # Return rows
    return "<p>Products:</p><ul>" + \
           "".join(["<li>" + row[0] + "</li>" for row in rows]) + \
           "</ul>  PID> " + str(os.getpid())




if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
