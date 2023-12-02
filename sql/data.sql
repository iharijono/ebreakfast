use ebreakfast_db;

-- CUSTOMERS 
INSERT INTO addresses (street, city, zip)
VALUES
    ('street 1', 'city 1', '00001'),
    ('street 2', 'city 2', '00002'),
    ('street 3', 'city 3', '00003'),
    ('street 4', 'city 4', '00004'),
    ('street 5', 'city 5', '00005'),
    ('street 6', 'city 6', '00006'),
    ('street 7', 'city 7', '00007'),
    ('street 8', 'city 8', '00008'),
    ('street 9', 'city 9', '00009');

INSERT INTO creditcards (id, numbers, zip)
VALUES
    ('creditcard_id_1', '0000000000000001', '00001'),
    ('creditcard_id_2', '0000000000000002', '00002'),
    ('creditcard_id_3', '0000000000000003', '00003'),
    ('creditcard_id_4', '0000000000000004', '00004'),
    ('creditcard_id_5', '0000000000000005', '00005'),
    ('creditcard_id_6', '0000000000000006', '00006'),
    ('creditcard_id_7', '0000000000000007', '00007'),
    ('creditcard_id_8', '0000000000000008', '00008'),
    ('creditcard_id_9', '0000000000000009', '00009');

INSERT INTO customers (id, email, phone, password, birthdate, address_fk)
VALUES
    ('test', 'test@email.com', '4086666661', 'secret', '2001-7-04', 1),
    ('customer_id_1', 'email1', '4086666662', 'secret', '2002-7-04', 2),
    ('customer_id_2', 'email2', '4086666662', 'secret', '2002-7-04', 2),
    ('customer_id_3', 'email3', '4086666663', 'secret', '2003-7-04', 3),
    ('customer_id_4', 'email4', '4086666664', 'secret', '2004-7-04', 4),
    ('customer_id_5', 'email5', '4086666665', 'secret', '2005-7-04', 5),
    ('customer_id_6', 'email6', '4086666666', 'secret', '2006-7-04', 6),
    ('customer_id_7', 'email7', '4086666667', 'secret', '2007-7-04', 7),
    ('customer_id_8', 'email8', '4086666668', 'secret', '2008-7-04', 8),
    ('customer_id_9', 'email9', '4086666669', 'secret', '2009-7-04', 9);

INSERT INTO admins (id, email, phone, password)
VALUES
    ('admin', 'admin@email.com', '4086666661', 'secret'),
    ('admin_1', 'email1@email.com', '4086666661', 'secret'),    
    ('admin_2', 'email2@email.com', '4086666662', 'secret'),
    ('admin_3', 'email3@email.com', '4086666663', 'secret'),
    ('admin_4', 'email4@email.com', '4086666664', 'secret'),
    ('admin_5', 'email5@email.com', '4086666665', 'secret'),
    ('admin_6', 'email6@email.com', '4086666666', 'secret'),
    ('admin_7', 'email7@email.com', '4086666667', 'secret'),
    ('admin_8', 'email8@email.com', '4086666668', 'secret'),
    ('admin_9', 'email9@email.com', '4086666669', 'secret');

INSERT INTO  paymentmethods (customer_fk, creditcard_fk)
VALUES
    ('customer_id_1', 'creditcard_id_1'),
    ('customer_id_2', 'creditcard_id_2'),
    ('customer_id_3', 'creditcard_id_3'),
    ('customer_id_4', 'creditcard_id_4'),
    ('customer_id_5', 'creditcard_id_5'),
    ('customer_id_6', 'creditcard_id_6'),
    ('customer_id_7', 'creditcard_id_7'),
    ('customer_id_8', 'creditcard_id_8'),
    ('customer_id_9', 'creditcard_id_9');

-- MERCHANT
INSERT INTO merchants (id, email, phone, tax_id)
VALUES
    ('merchant_id_1', 'merchant_email1', '5086666661', 'tax_id1'),
    ('merchant_id_2', 'merchant_email2', '5086666662', 'tax_id2'),
    ('merchant_id_3', 'merchant_email3', '5086666663', 'tax_id3'),
    ('merchant_id_4', 'merchant_email4', '5086666664', 'tax_id4'),
    ('merchant_id_5', 'merchant_email5', '5086666665', 'tax_id5'),
    ('merchant_id_6', 'merchant_email6', '5086666666', 'tax_id6'),
    ('merchant_id_7', 'merchant_email7', '5086666667', 'tax_id7'),
    ('merchant_id_8', 'merchant_email8', '5086666668', 'tax_id8'),
    ('merchant_id_9', 'merchant_email9', '5086666669', 'tax_id9');

-- RESTAURANT
INSERT INTO restaurants (id, email, phone, merchant_fk)
VALUES
    ('ebreakfast', 'email@ebreakfast.com', '4086666661', 'merchant_id_1'),
    ('restaurant_id_2', 'email2', '4086666662', 'merchant_id_2'),
    ('restaurant_id_3', 'email3', '4086666663', 'merchant_id_3'),
    ('restaurant_id_4', 'email4', '4086666664', 'merchant_id_4'),
    ('restaurant_id_5', 'email5', '4086666665', 'merchant_id_5'),
    ('restaurant_id_6', 'email6', '4086666666', 'merchant_id_6'),
    ('restaurant_id_7', 'email7', '4086666667', 'merchant_id_7'),
    ('restaurant_id_8', 'email8', '4086666668', 'merchant_id_8'),
    ('restaurant_id_9', 'email9', '4086666669', 'merchant_id_9');

-- MEAL
INSERT INTO meals (id, descr, price, restaurant_fk)
VALUES
    ('burger', 'desc_meal_1', 10.25, 'ebreakfast'),
    ('coffee', 'desc_meal_2', 2.25, 'ebreakfast'),
    ('omelette', 'desc_meal_3', 13.25, 'ebreakfast'),
    ('pancake', 'desc_meal_4', 4.25, 'ebreakfast'),
    ('pizza', 'desc_meal_5', 15.25, 'ebreakfast'),
    ('toast', 'desc_meal_6', 3.25, 'ebreakfast'),
    ('meal_id_7', 'desc_meal_7', 7.25, 'ebreakfast'),
    ('meal_id_8', 'desc_meal_8', 8.25, 'ebreakfast'),
    ('meal_id_9', 'desc_meal_9', 9.25, 'ebreakfast');

-- ORDERS

-- INSERT INTO orders (customer_fk)
-- VALUES
-- 	('customer_id_1'),
-- 	('customer_id_2'),
-- 	('customer_id_3'),
-- 	('customer_id_4'),
-- 	('customer_id_5'),
-- 	('customer_id_6'),
-- 	('customer_id_7'),
-- 	('customer_id_8'),
-- 	('customer_id_9');
	
-- INSERT INTO ordermeals (order_fk, meal_fk)
-- VALUES
-- 	(1, 'meal_id_1'),
-- 	(2, 'meal_id_2'),
-- 	(3, 'meal_id_3'),
-- 	(4, 'meal_id_4'),
-- 	(5, 'meal_id_5'),
-- 	(6, 'meal_id_6'),
-- 	(7, 'meal_id_7'),
-- 	(8, 'meal_id_8'),
-- 	(9, 'meal_id_9');


