from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world! This app was built by Ben on 9/2/21!! The following changes were made for testing CI/CD.'
