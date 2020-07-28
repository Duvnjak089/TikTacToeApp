from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_docker():
    return render_template("test_website.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
