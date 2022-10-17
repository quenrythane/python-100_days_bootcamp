from flask import Flask, render_template, request
import requests as req
from mail.mail_sender import send_message


url = "https://api.npoint.io/c790b4d5cab58020d391"  # [{id, body, title, subtitle}, ...]
blog_response = req.get(url).json()

app = Flask(__name__)


@app.route('/blog')
@app.route('/')
def home():
    return render_template("index.html",
                           posts=blog_response)


@app.route('/post/<int:index>')
def post(index):
    post_data = blog_response[index-1]
    return render_template("post.html",
                           title=post_data["title"],
                           body=post_data["body"],
                           subtitle=post_data["subtitle"])


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(request.form)
        send_message(email, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



# Flask app start here
if __name__ == "__main__":
    app.run(debug=True, port=100)
