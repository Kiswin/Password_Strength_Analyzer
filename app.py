from flask import Flask, request
from password_analyzer import analyze_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        pwd = request.form["password"]
        result, _ = analyze_password(pwd)

    return f"""
    <h2>Password Strength Analyzer</h2>
    <form method="post">
        <input type="password" name="password" placeholder="Enter password">
        <button type="submit">Check</button>
    </form>
    <h3>{result}</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)