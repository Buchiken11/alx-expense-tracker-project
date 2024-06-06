from flask import redirect, url_for, session, request
from flask_login import login_user, logout_user, login_required
from oauth import google
from models import User, users

def setup_routes(app):

    @app.route('/')
    def index():
        return 'Welcome to the Expense Tracker!'

    @app.route('/login')
    def login():
        return redirect(url_for('google_login'))

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/login/google')
    def google_login():
        return google.authorize(callback=url_for('google_authorized', _external=True))

    @app.route('/login/google/authorized')
    def google_authorized():
        response = google.authorized_response()
        if response is None or response.get('access_token') is None:
            return 'Access denied: reason={} error={}'.format(
                request.args['error_reason'],
                request.args['error_description']
            )

        session['google_token'] = (response['access_token'], '')
        userinfo = google.get('userinfo')
        user_data = userinfo.data
        user = User(id=user_data['id'], name=user_data['name'], email=user_data['email'])
        users[user.id] = user
        login_user(user)
        return redirect(url_for('index'))

    @google.tokengetter
    def get_google_oauth_token():
        return session.get('google_token')
