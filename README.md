# Django Customer and Order Management

# Overview of the system
This project is a simple Django application that manages Customer and Order models. It implements a one-to-many relationship where each customer can place multiple orders, and each order is linked to a single customer.

# Features
Models:
Customer: customer_name, customer_email, updated_at.
Order: customer, order_date, total_amount_of_order, updated_at.
Seamless relationship management between Customer and Order.

# Setting up the environment and running the project.

# 1. Create a virtual environment:
python -m venv venv
.\venv\Scripts\activate.ps1

# 2. Apply database migrations:
python manage.py migrate

# 3. Start the development server:
python manage.py runserver

# 4. Access the application: Open http://127.0.0.1:8000 in your browser.

# 5. View the SQL migration statements:
py manage.py sqlmigrate CAT2 0001

   

  
