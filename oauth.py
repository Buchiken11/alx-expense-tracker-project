from flask_oauthlib.client import OAuth

oauth = OAuth()

google = oauth.remote_app(
    'google',
    consumer_key='your-google-client-id',
    consumer_secret='your-google-client-secret',
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accoufewnts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

# Add other providers similarly

def init_oauth(app):
    oauth.init_app(app)
