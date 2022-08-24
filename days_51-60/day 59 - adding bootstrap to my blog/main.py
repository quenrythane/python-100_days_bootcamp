from flask import Flask, render_template
from datetime import datetime
import requests as req

app = Flask(__name__)
now_date = datetime.now().date()


@app.route('/')
def home():
    art_name = 'Art'
    return render_template('index.html',
                           name=art_name,
                           date=now_date)


@app.route('/guess/<name>')
def guess(name):
    name = name.capitalize()
    url = f"https://api.genderize.io?name={name}"
    response = req.get(url)
    gender = response.json()["gender"]
    return render_template('guess.html',
                           name=name,
                           gender=gender,
                           date=now_date)


@app.route('/blog/<num>')
def blog_function(num):

    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = req.get(blog_url)
    all_posts = blog_response.json()
    return render_template('blog.html',
                           posts=all_posts,
                           num=num,
                           date=now_date)



if __name__ == "__main__":
    app.run(debug=True)
