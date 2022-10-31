from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mysqldb import MySQL
from config import config
#models
from models.ModelUser import ModelUser
#entities
from models.entities.User import User


app=Flask(__name__)
db=MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        user = User(0, username, password)
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('home'))
            else:
                return render_template('auth/login.html')
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
    



def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,page_not_found)
    app.run()