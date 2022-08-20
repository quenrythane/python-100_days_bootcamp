from flask import Flask, render_template
import requests as req

app = Flask(__name__)
url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = req.get(url).json()


@app.route('/blog')
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


if __name__ == "__main__":
    app.run(debug=True)
