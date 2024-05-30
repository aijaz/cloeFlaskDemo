from flask import Flask
import psycopg2
import psycopg2.extras

my_flask_app = Flask(__name__)


@my_flask_app.route("/cloe")
def cloe():
    return "Hello, Cloe"


@my_flask_app.route("/employees")
def employees():
    # connect to the database
    con = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="mysecretpassword",
        host="aijaz_pg_c"
    )

    # create a cursor
    cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    # get the data
    cur.execute("select * from employee")
    result = cur.fetchall()

    # commit and close the database connection
    con.close()
    # return the data
    return result


if __name__ == "__main__":
    my_flask_app.run(host='0.0.0.0', port=8000, debug=True)
