import os

class Config:
    SECRET_KEY = os.urandom(24)
    GOOGLE_CLIENT_ID = '498539836001-jndkm3uv65gugb5eg6l3m7idj35ve5o2.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'
    FACEBOOK_CLIENT_ID = 'your-facebook-client-id'
    FACEBOOK_CLIENT_SECRET = 'your-facebook-client-secret'
    TWITTER_CLIENT_ID = 'your-twitter-client-id'
    TWITTER_CLIENT_SECRET = 'your-twitter-client-secret'
    LINKEDIN_CLIENT_ID = 'your-linkedin-client-id'
    LINKEDIN_CLIENT_SECRET = 'your-linkedin-client-secret'

