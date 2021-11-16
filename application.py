from flask import Flask, render_template
app = application = Flask(__name__)

@app.route('/')
def home():
    return render_template('todo.html')