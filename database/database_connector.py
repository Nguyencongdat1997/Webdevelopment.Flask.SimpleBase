from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import load_only

from database.database_setup import Base, Account


class DatabaseConnectorBase(object):
	
	def __init__(self):
		# Create session and connect to DB
		engine = create_engine('sqlite:///flaskserverbase.db')
		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		self.session = DBSession()


class  AccountConnector(DatabaseConnectorBase):

	def __init__(self):
		super( AccountConnector, self).__init__()

	def insert_one(self, account, password, role):
		#check duplicate:
		if len(self.get_one(account)) > 0:
			print('Duplicated when inserting account: ' + account)
			return None

		new_account = Account(account = account, password = password, role = role)
		self.session.add(new_account)
		self.session.commit()

	def update_one_role(self, account, new_role):
		
		self.session.query(Account).filter_by(account = account).update({'role': new_role})		
		self.session.commit()	

	def delete_one(self, account):
		self.session.query(Account).filter_by(account = account).delete()
		self.session.commit()

	def get_one(self, account):
		list_accouts = []
		for x in self.session.query(Account).filter_by(account = account):
			list_accouts.append(dict(account = x.account, password = x.password, role = x.role))
		return list_accouts

	def get_all(self):
		list_account = []
		for x in self.session.query(Account):
			list_account.append(dict(account = x.account, password = x.password, role = x.role))
		return list_account

	def get_by_role(self, role):		
		list_accouts = []	
		for x in self.session.query(Account).filter_by(role = role):
			list_accouts.append(dict(account = x.account, password = x.password, role = x.role))
		return list_accouts

	def validate_password(self, account, password):
		data = self.session.query(Account.account, Account.password).filter_by(account = account)
		if data == None or data.first() == None:
			return False
		data_acc, data_pass = data.first()
		return (account == data_acc and password == data_pass)