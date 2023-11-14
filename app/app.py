'''
Created on Fri Sept 22, 2023

@author: Aristoteles
'''

import sys
import json

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database
import solara.server.flask


app = Flask(__name__)
app.register_blueprint(solara.server.flask.blueprint, url_prefix="/solara/")

app.secret_key = "mys3cr3tk3y"
db = Database()

@app.route('/')
def index():
    data = db.read(None)
    return render_template('index.html', data = data)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addcustomer', methods = ['POST', 'GET'])
def addcustomer():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new customer has been added")
        else:
            flash("A new customer can not be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<string:id>/')
def update(id):
    data = db.read(id)

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatecustomer', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A customer has been updated')

        else:
            flash('A customer can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<string:id>/')
def delete(id):
    data = db.read(id)

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletecustomer', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A customer has been deleted')

        else:
            flash('A customer can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
