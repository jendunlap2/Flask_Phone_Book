from app import app
from flask import render_template, redirect, url_for
from app.forms import RegisterForm

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        phone_num = form.phone_num.data
        address = form.address.data
        print(name, phone_num, address)
        return redirect(url_for('success'))
        
    return render_template('register.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')