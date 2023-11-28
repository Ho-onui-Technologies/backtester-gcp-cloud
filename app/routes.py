from google.auth.transport import requests
from google.oauth2 import id_token
from flask import Flask, request, abort

from app import app


@app.route('/')
def index():
    # Get the ID token from the request header
    id_token_header = request.headers.get('Authorization')

    if id_token_header:
        # Extract the token from the header
        token = id_token_header.split(' ').pop()

        try:
            # Verify the token
            id_info = id_token.verify_oauth2_token(token, requests.Request())

            # Token is valid, process the request
            return "Hello, authenticated user!"

        except ValueError:
            # Invalid token
            abort(403)
    else:
        # No token provided
        abort(401)