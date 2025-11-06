from flask import Flask, render_template, request, redirect, url_for, session, flash
from collections import defaultdict

app = Flask(__name__)
app.secret_key = "CHANGE_ME_TO_A_RANDOM_SECRET"  # needed for sessions

# Very simple "user database"
USERS = {
    "user1": "pass1",
    "user2": "pass2",
}

# Visit counter per user (in-memory)
VISITS = defaultdict(int)

def login_required(fn):
    from functools import wraps
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            flash("Please log in first.")
            return redirect(url_for("login"))
        return fn(*args, **kwargs)
    return wrapper

@app.route("/", methods=["GET"])
def home():
    # Redirect to login or dashboard based on session
    if "username" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if username in USERS and USERS[username] == password:
            session["username"] = username
            flash(f"Welcome, {username}!")
            # First entry into dashboard will count as visit
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password.")
            return render_template("login.html")

    return render_template("login.html")

@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    username = session["username"]
    # Increment visit count *each time* dashboard is viewed
    VISITS[username] += 1
    count = VISITS[username]
    return render_template("dashboard.html", username=username, count=count)

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    flash("Logged out successfully.")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
