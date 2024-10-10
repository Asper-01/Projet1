from flask import Flask

app = Flask("ISC")

@app.route('/')
def bonjour():
    return "<h1> Hello !</h1>"


app.run()
