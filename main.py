from flask import Flask, render_template
import random
import datetime
import requests

agify = "https://api.agify.io"
genderize = "https://api.genderize.io?"

app = Flask(__name__)

@app.route("/")
def home():
    rand_no = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html", num = rand_no, year = year)

@app.route("/guess/<name>")
def guess(name):
    params = {
        "name":name
    }

    agify_ = requests.get(url=agify, params=params)
    age = agify_.json()['age']

    gender_ = requests.get(url=genderize, params=params)
    gender = gender_.json()['gender']

    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    blog = requests.get("https://api.npoint.io/765925b48d59dda74f32")
    all_post = blog.json()
    return render_template("blog.html", all_posts = all_post)



if __name__ == "__main__":
    app.run(port=8000, debug=True)