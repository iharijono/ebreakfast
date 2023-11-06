#
# requires: sqlacodegen
# generated by: sqlacodegen mysql+pymysql://root:root@localhost/ebreakfast_db --outfile models.py


import models
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# # from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base


# engine = create_engine("mysql+pymysql://root:root@localhost/ebreakfast_db", echo=True, future=True)
engine = create_engine("mysql+pymysql://root:root@localhost/ebreakfast_db", future=True)
with Session(engine) as session:
    add1 = models.Address(street='street10112', city='city101', zip='55555')
    cc1 = models.Creditcard(id='cc111122', numbers='444444444444444', zip='44444')
    session.add(add1)
    session.commit()  
    session.add(cc1)
    print(f'---> {add1.id}')
    cust1 = models.Customer(id='cust111112', email='cust1@example.com', phone='3333333333', birthdate='2000-7-07', address_fk=add1.id)
    session.add(cust1)
    session.commit()
