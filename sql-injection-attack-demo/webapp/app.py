from flask import Flask, request, render_template
import psycopg
import os

app = Flask(__name__)

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_NAME = os.getenv("DATABASE_NAME", "demo")
DATABASE_USER = os.getenv("DATABASE_USER", "demo_user")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "demo_password")

def query_db(query):
    try:
        conn_str = (
            f"host={DATABASE_HOST} dbname={DATABASE_NAME} user={DATABASE_USER} password={DATABASE_PASSWORD}"
        )
        with psycopg.connect(conn_str) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                results = cur.fetchall()
            conn.commit()
        return results
    except Exception as e:
        return [str(e)]

@app.route("/search", methods=["GET"])
def search():
    results = None
    user_id = request.args.get("id", "")  
    if user_id:
        query = f"SELECT * FROM bookings WHERE id = {user_id};"
        results = query_db(query)
    return render_template("search.html", results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

