from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world! This app was built by Ben on 9/2/21!! And here are some changes that were added after the app was run for the first time. Pretty neat, huh?'
