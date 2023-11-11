# app/routes.py

from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Customer
from solara import Solara
from app.database import Database

solara = Solara(app)
database = Database()

@app.route('/')
def index():
    customers = database.read_customers()
    return solara.render(Customer, customers)

@app.route('/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        data = {
            'id': request.form['id'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'birthdate': request.form['birthdate']
        }
        if database.insert_customer(data):
            flash('Customer added successfully', 'success')
        else:
            flash('Failed to add customer', 'danger')

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/update/<string:customer_id>', methods=['GET', 'POST'])
def update_customer(customer_id):
    if request.method == 'POST':
        data = {
            'id': request.form['id'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'birthdate': request.form['birthdate']
        }
        if database.update_customer(customer_id, data):
            flash('Customer updated successfully', 'success')
        else:
            flash('Failed to update customer', 'danger')

        return redirect(url_for('index'))

    customer = database.read_customer_by_id(customer_id)
    if customer:
        return render_template('update.html', customer=customer[0])
    else:
        flash('Customer not found', 'danger')
        return redirect(url_for('index'))

@app.route('/delete/<string:customer_id>', methods=['GET', 'POST'])
def delete_customer(customer_id):
    if request.method == 'POST':
        if database.delete_customer(customer_id):
            flash('Customer deleted successfully', 'success')
        else:
            flash('Failed to delete customer', 'danger')

        return redirect(url_for('index'))

    customer = database.read_customer_by_id(customer_id)
    if customer:
        return render_template('delete.html', customer=customer[0])
    else:
        flash('Customer not found', 'danger')
        return redirect(url_for('index'))
