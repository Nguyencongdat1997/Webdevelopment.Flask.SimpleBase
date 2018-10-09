from flask import Flask, session, render_template, abort, request, redirect, jsonify, url_for
from functools import wraps

from controllers.account_controller import account_controller

app = Flask(__name__)
app.register_blueprint(account_controller)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if (not session.get('logged_in')) or (not session['logged_in']):
            return redirect(url_for('account_controller.show_login', next_page = request.url[7:]))
        return f(*args, **kwargs)
    return decorated_function


@app.errorhandler(401)
def page_not_found(e):
	return render_template('401.html'), 401


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
	account_info = session.get('account_info', None)
	return render_template('home.html', account = account_info['account'])


if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)