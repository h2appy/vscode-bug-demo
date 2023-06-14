from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Add breakpoint here")
    return 'Hello, project-b.'
