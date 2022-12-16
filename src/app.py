from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
from config import config

#models
from models.ModelUser import ModelUser
#entities
from models.entities.User import User

app = Flask(__name__)

db = MySQL(app)

csfr = CSRFProtect()

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
@login_required
def system():
    return render_template('system.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


def page_not_found(error):
    return render_template('404.html'), 404

def unauthorised(error):
    return render_template('unauthorised.html'), 401

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csfr.init_app(app)
    app.register_error_handler(404,page_not_found)
    app.register_error_handler(401,unauthorised)
    app.run()