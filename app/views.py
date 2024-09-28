from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User
from flask_login import login_user, login_required, logout_user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('form'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        age = request.form['age']
        bio = request.form['bio']

        # Validate input
        if not username or not password or not name or not age:
            flash('Please fill in all required fields.')
            return redirect(url_for('register'))

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('register'))

        # Create new user
        user = User(username=username, password=password, name=name, age=age, bio=bio)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful. Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/form', methods=['GET', 'POST'])
@login_required
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        bio = request.form['bio']

        # Validate input
        if not name or not age:
            flash('Please fill in all required fields.')
            return redirect(url_for('form'))

        # Update current user's data
        current_user.name = name
        current_user.age = age
        current_user.bio = bio
        db.session.commit()

        flash('Data saved successfully!')
        return redirect(url_for('display'))

    return render_template('form.html', user=current_user)

@app.route('/display', methods=['GET', 'POST'])
@login_required
def display():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = User.query.get(user_id)
        if user and user != current_user:
            flash('You cannot delete another user\'s data.')
        elif user:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted successfully.')
        return redirect(url_for('display'))

    users = User.query.all()
    return render_template('display.html', users=users)