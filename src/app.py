from flask import Flask, render_template
from config import config


app=Flask(__name__)

@app.route('/')
def init():
    return render_template('layout.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()