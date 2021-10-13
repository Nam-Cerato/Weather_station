from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_pymongo import PyMongo
from flask_login import login_required, current_user
import json
from app.models import *

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session.pop('user', None)
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if(len(get_userByUserName(username)) == 1):
            password_correct = get_userByUserName('nam')[0]['password']
            print("password_correct", password_correct)
            if(password == password_correct):
                print("pass correct")
                return redirect(url_for('views.hanoi'))
            else:
                flash('The username or password is incorrect!')
        else:
                flash('The username or password is incorrect!')
    return render_template('login.html', the_title='login')

@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', the_title='Tiger in Myth and Legend')

@views.route('/map')
def map():
    return render_template('map.html', the_title='Tiger in Myth and Legend')

@views.route('/notifications')
def notifications():
    return render_template('notifications.html', the_title='Tiger in Myth and Legend')

@views.route('/user')
def user():
    return render_template('user.html', the_title='Tiger in Myth and Legend', data = 1)

@views.route('/hanoi')
def hanoi():
    return render_template('hanoi.html', the_title='Weather station')

@views.route('/tphcm')
def tphcm():
    return render_template('tphcm.html', the_title='Weather station')

@views.route('/hanoi/farm1')
def hanoi_farm1():
    return render_template('hanoi/farm1.html', the_title='Weather station')

@views.route('/hanoi/farm2')
def hanoi_farm2():
    return render_template('hanoi/farm2.html', the_title='Weather station')

@views.route('/hanoi/farm3')
def hanoi_farm3():
    return render_template('hanoi/farm3.html', the_title='Weather station')


@views.route('/tphcm/farm1')
def tphcm_farm1():
    return render_template('tphcm/farm1.html', the_title='Weather station')
    
@views.route('/tphcm/farm2')
def tphcm_farm2():
    return render_template('tphcm/farm2.html', the_title='Weather station')
    
@views.route('/tphcm/farm3')
def tphcm_farm3():
    return render_template('tphcm/farm3.html', the_title='Weather station')
    
@views.route('/tphcm/farm4')
def tphcm_farm4():
    return render_template('tphcm/farm4.html', the_title='Weather station')
