from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
#models
from models.ModelUser import ModelUser
#entities
from models.entities.User import User

app=Flask(__name__)

db=MySQL(app)

login_manager_app=LoginManager(app)
                                                
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    data={'nouser':True}
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        user = User(0, username, password)
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('system'))
            else:
                return render_template('auth/login.html',data=data)
        else:
            return render_template('auth/login.html',data=data)
    else:
        return render_template('auth/login.html',data=False)

@app.route('/app')
def system():
    return render_template('system.html')

def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,page_not_found)
    app.run()