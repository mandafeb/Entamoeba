from flask import Blueprint

microblog = Blueprint('model', __name__)

@microblog.route('/')
@microblog.route('/index')
def index():
    return 'Hello, world!'