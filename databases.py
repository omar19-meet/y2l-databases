from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, price, sold_out):
	product_object= Product(
		name=name,
		price=price,
		sold_out=sold_out)
	session.add(product_object)
	session.commit()

def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(id):
	print('Cheese')
	session.query(Product).filter_by(
		id=id).delete()
	session.commit()

def get_product(id):
  pass

# create_product('Watch',500,False)
delete_product(2)