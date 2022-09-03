from flask import Flask, render_template, request, redirect, url_for, flash, session 


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')



if __name__ == "__main__":
    #verDebug = True if (os.environ.get('Debug', "True")) == "True") else  False
    app.run(debug=True,host= '127.0.0.1' , port=8080)