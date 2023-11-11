# app/routes.py

from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Customer
from solara import Solara
from app.database import Database

# Initialize Solara and Database instances
solara = Solara(app)
database = Database()

# Route for displaying the list of customers
@app.route('/')
def index():
    # Read the list of customers from the database
    customers = database.read_customers()
    # Render the list of customers using Solara
    return solara.render(Customer, customers)

# Route for adding a new customer
@app.route('/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        # Extract data from the form
        data = {
            'id': request.form['id'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'birthdate': request.form['birthdate']
        }
        # Insert the new customer into the database
        if database.insert_customer(data):
            flash('Customer added successfully', 'success')
        else:
            flash('Failed to add customer', 'danger')

        return redirect(url_for('index'))

    # Render the add customer form
    return render_template('add.html')

# Route for updating an existing customer
@app.route('/update/<string:customer_id>', methods=['GET', 'POST'])
def update_customer(customer_id):
    if request.method == 'POST':
        # Extract data from the form
        data = {
            'id': request.form['id'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'birthdate': request.form['birthdate']
        }
        # Update the customer in the database
        if database.update_customer(customer_id, data):
            flash('Customer updated successfully', 'success')
        else:
            flash('Failed to update customer', 'danger')

        return redirect(url_for('index'))

    # Read the customer from the database by ID and render the update form
    customer = database.read_customer_by_id(customer_id)
    if customer:
        return render_template('update.html', customer=customer[0])
    else:
        flash('Customer not found', 'danger')
        return redirect(url_for('index'))

# Route for deleting an existing customer
@app.route('/delete/<string:customer_id>', methods=['GET', 'POST'])
def delete_customer(customer_id):
    if request.method == 'POST':
        # Delete the customer from the database
        if database.delete_customer(customer_id):
            flash('Customer deleted successfully', 'success')
        else:
            flash('Failed to delete customer', 'danger')

        return redirect(url_for('index'))

    # Read the customer from the database by ID and render the delete form
    customer = database.read_customer_by_id(customer_id)
    if customer:
        return render_template('delete.html', customer=customer[0])
    else:
        flash('Customer not found', 'danger')
        return redirect(url_for('index'))
