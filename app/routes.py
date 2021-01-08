from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Iván'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():   # Procesa el formulario
        flash('Login requested for user {}, remember_me={}'.format(   # Guarda el mensaje
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))   # respuesta al navegador para que redireccione a otra URL
    return render_template('login.html', title='Sign In', form=form)
