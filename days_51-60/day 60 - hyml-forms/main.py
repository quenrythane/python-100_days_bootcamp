from flask import Flask, render_template, request
import requests as req

app = Flask(__name__)
url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = req.get(url).json()


@app.route('/form')
@app.route('/')
def home():
    return render_template("index.html")


@app.route("/something/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    print(request.form)

    return f"<h1>Name: {name}, Password: {password}xd</h1>"


# App starts here
if __name__ == "__main__":
    app.run(debug=True, port=60)
