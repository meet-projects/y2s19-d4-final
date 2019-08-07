from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Donor(Base):
	__tablename__ = 'donors'
	donor_id = Column(Integer,primary_key=True)
	donor_first_name = Column(String)
	donor_last_name = Column(String)
	donor_email = Column(String)
	donor_message = Column(String)
	def __repr__(self):
		return ("Donor's First Name: {}\n"
				"Donor's Last Name: {}\n"
				"Donor's email: {}\n"
				"Donor's message: {}\n"
				"ID: {}").format(
					self.donor_first_name,
					self.donor_last_name,
					self.donor_email,
					self.donor_message,
					self.donor_id)