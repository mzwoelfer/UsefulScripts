from flask import Flask, request, render_template, redirect, url_for
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


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        query = f"""
        SELECT id FROM customers 
        WHERE username = '{username}' AND password = '{password}';
        """
        results = query_db(query)
        if results:
            user_id = results[0][0]  
            return redirect(url_for("profile", id=user_id))
        else:
            return "Invalid username or password", 401
    return render_template("login.html")

@app.route("/profile", methods=["GET"])
def profile():
    user_id = request.args.get("id", "")
    if user_id:
        query = f"SELECT * FROM customers WHERE id = {user_id};"
        results = query_db(query)
        return render_template("profile.html", results=results)
    return "No user ID provided", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
