from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home2():
    return render_template('home.html')

@app.route("/jag")
def home():
    return render_template('jag.html')

@app.route('/sida2')
def sida2():
    return render_template('sida2.html')


#if __name__ == "__main__":
#    app.run(debug=True)



if __name__ == "__main__":
    app.run()