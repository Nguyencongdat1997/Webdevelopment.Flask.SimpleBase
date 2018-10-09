from database.database_connector import AccountConnector

accountConnector = AccountConnector()

#insert
accountConnector.insert_one(account = 'account1', password = '1', role = 'admin')
accountConnector.insert_one(account = 'account2', password = '1', role = 'user')
accountConnector.insert_one(account = 'account3', password = '1', role = 'user')

#query
for x in accountConnector.get_all():
	print (x)

#update 
accountConnector.update_one_role(2, 'admin')
for x in accountConnector.get_all():
	print (x)

#delete
accountConnector.delete_one(2)
for x in accountConnector.get_all():
	print (x)

#validate password
print(accountConnector.validate_password('account1', '1'))
print(accountConnector.validate_password('account1', '2'))