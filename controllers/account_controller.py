from flask import Blueprint, session, render_template, abort, request, redirect, jsonify, url_for
from database.database_connector import AccountConnector

account_controller = Blueprint('account_controller', __name__, template_folder='/templates')


@account_controller.route('/showlogin', methods=['GET', 'POST'])
def show_login():
	error_message = request.args.get('error_message', None)
	next_page = request.args.get('next_page', '/home')
	return render_template('login.html', error_message = error_message, next_page = next_page)


@account_controller.route('/checklogin', methods=['POST'])
def check_login():
	if request.method == 'POST':
		if request.form['account'] and request.form['password'] and request.form['next_page']:
			account = request.form['account']
			password = request.form['password']
			next_page = request.form['next_page']
		else:
			abort(401)
	else:
		abort(401)
	account_connector = AccountConnector()
	if account_connector.validate_password(account, password):
		session['logged_in'] = True
		session['account_info'] = account_connector.get_one(account)[0]		
		return redirect(next_page)
	else:
		return redirect(url_for('account_controller.show_login', error_message = 'Invalid account or password', next_page = next_page))


@account_controller.route('/logout', methods=['GET', 'POST'])
def logout():
	session['logged_in'] = False
	session['account_info'] = None

	return redirect('/showlogin')