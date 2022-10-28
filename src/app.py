from flask import Flask, render_template, request
from config import config


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        print(request.form['user'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')



def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,page_not_found)
    app.run()