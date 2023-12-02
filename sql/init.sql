CREATE DATABASE IF NOT EXISTS ebreakfast_db;
use ebreakfast_db;

-- CUSTOMERS 
CREATE TABLE IF NOT EXISTS addresses (
  id INT PRIMARY KEY AUTO_INCREMENT,
  street VARCHAR(80) NOT NULL,
  city VARCHAR(20) NOT NULL,
  zip VARCHAR(20) NOT NULL,
  country VARCHAR(80) DEFAULT 'United States'
);

CREATE TABLE IF NOT EXISTS creditcards (
  id VARCHAR(80) PRIMARY KEY,
  numbers VARCHAR(80) NOT NULL,
  zip VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
  id VARCHAR(20) PRIMARY KEY,
  email VARCHAR(20),
  phone VARCHAR(20),
  birthdate DATE,
  password VARCHAR(80),
  address_fk INT NOT NULL,
  FOREIGN KEY (address_fk)
    REFERENCES addresses (id)
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS admins (
  id VARCHAR(20) PRIMARY KEY,
  email VARCHAR(20),
  phone VARCHAR(20),
  password VARCHAR(80)
);

CREATE TABLE IF NOT EXISTS paymentmethods (
  customer_fk VARCHAR(20) NOT NULL,
  creditcard_fk VARCHAR(80) NOT NULL,
  FOREIGN KEY (customer_fk)
    REFERENCES customers (id)
    ON DELETE CASCADE,
  FOREIGN KEY (creditcard_fk)
    REFERENCES creditcards (id)
    ON DELETE CASCADE
);

-- MERCHANT
CREATE TABLE IF NOT EXISTS merchants (
  id VARCHAR(20) PRIMARY KEY,
  email VARCHAR(20),
  phone VARCHAR(20),
  tax_id VARCHAR(20)
);

-- RESTAURANT
CREATE TABLE IF NOT EXISTS restaurants (
  id VARCHAR(20) PRIMARY KEY,
  email VARCHAR(20),
  phone VARCHAR(20),
  merchant_fk VARCHAR(20) NOT NULL,
  FOREIGN KEY (merchant_fk)
    REFERENCES merchants (id)
    ON DELETE CASCADE
);

-- MEAL
CREATE TABLE IF NOT EXISTS meals (
  id VARCHAR(20) PRIMARY KEY,
  descr VARCHAR(80),
  price DOUBLE(5,2),
  restaurant_fk VARCHAR(20) NOT NULL,
  FOREIGN KEY (restaurant_fk)
    REFERENCES restaurants (id)
    ON DELETE CASCADE
);

-- ORDERS

CREATE TABLE IF NOT EXISTS orders (
  id INT PRIMARY KEY AUTO_INCREMENT,
  customer_fk VARCHAR(20) NOT NULL,
  FOREIGN KEY (customer_fk)
    REFERENCES customers (id)
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ordermeals (
  order_fk INT NOT NULL,
  quantity INT,
  meal_fk VARCHAR(20) NOT NULL,
  FOREIGN KEY (order_fk)
    REFERENCES orders (id)
    ON DELETE CASCADE,
  FOREIGN KEY (meal_fk)
    REFERENCES meals (id)
    ON DELETE CASCADE
);

