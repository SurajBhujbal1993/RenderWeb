from flask import Flask, render_template_string
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # return render_template_string("<h1>{{ msg }}</h1>", msg="Hello from Python!")
    return render_template("index.html", msg="Samarth Class.")


if __name__ == "__main__":
    app.run(debug=True)
    