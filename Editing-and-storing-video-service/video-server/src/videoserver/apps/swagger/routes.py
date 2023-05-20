from flask import current_app as app
from flask import render_template, jsonify
from flask_swagger import swagger
from flask import Blueprint, request, Response
from . import bp

# Define a list of valid username and password combinations
users = {
    "admin": "password123",
    "user": "pass456"
}

@bp.route('/spec')
def spec_data():
    # Check if the request contains valid credentials
    auth = request.authorization
    if not auth or not (auth.username in users and auth.password == users[auth.username]):
        # If not, return a 401 Unauthorized error
        return Response('Could not verify your access level for that URL.\n'
                        'You have to login with proper credentials', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})
    
    swag = swagger(app)
    swag['info']['version'] = "0.1"
    swag['info']['title'] = "Video editor API"
    return jsonify(swag)


@bp.route('/')
def swag():
    # Check if the request contains valid credentials
    auth = request.authorization
    if not auth or not (auth.username in users and auth.password == users[auth.username]):
        # If not, return a 401 Unauthorized error
        return Response('Could not verify your access level for that URL.\n'
                        'You have to login with proper credentials', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})
    
    return render_template('index.html')