from model import Base, Donor

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///donors.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_donor(first_name,last_name,email,message):

	donor_object = Donor(
			donor_first_name = first_name,
			donor_last_name = last_name,
			donor_email = email,
			donor_message = message)
	session.add(donor_object)
	session.commit()
def query_all():
	return session.query(Donor).all()
def delete_by_name(first_name,last_name):
	session.query(Donor).filter_by(donor_first_name=donor_first_name).filter_by(donor_last_name = last_name).delete()
	session.commit()
def delete_all():
	session.query(Donor).delete()
	session.commit()
