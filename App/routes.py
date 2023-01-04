from App import app, db, login_manager
from flask import render_template, url_for, redirect, request, flash
from App.models import User, Matches
from App.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/dijkstra')
def dijkstra_page():
    return render_template('dijkstra.html')


@app.route('/maze')
def maze_page():
    return render_template('maze.html')


@app.route('/new')
def new_page():
    return render_template('new.html')


@app.route('/ranking')
def ranking_page():
    items = [
        {'position': 1, 'name': 'Maciek', 'points': 12},
        {'position': 2, 'name': 'Beata', 'points': 9},
        {'position': 3, 'name': 'Tomek', 'points': 8},
        {'position': 4, 'name': 'Wojtek', 'points': 7},
        {'position': 5, 'name': 'Szymon', 'points': 6},
        {'position': 6, 'name': 'Janek', 'points': 5},
        {'position': 7, 'name': 'Kuba', 'points': 0}
    ]
    return render_template('ranking.html', items = items)


@app.route('/users')
def users_page():
    users = User.query.all()
    return render_template('users.html', items = users)


@app.route('/matches')
def matches_page():
    matches = Matches.query.all()
    return render_template('matches.html', items = matches)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category = 'success')
            return redirect(url_for('matches_page'))
        else:
            flash('Username or/and password is wrong! Please try again', category='danger')
    return render_template('login.html', form = form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('home_page'))


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(      username = form.username.data, 
                                    email = form.email_address.data, 
                                    password = form.password.data  )
        db.session.add(user_to_create)
        db.session.commit()
        # return redirect(url_for('users_page'))
        return redirect(url_for('login_page'))

    if form.errors:  #### IF THERE ARE NO ERRORS FROM THE VALIDATIONS
        for err in form.errors.values():
            flash(f'There was an error while creating a user: {err}', category='danger')

    return render_template('register.html', form = form)

