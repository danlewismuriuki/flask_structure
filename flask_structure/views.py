from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def main_index():
    return 'Blueprint views.py Hello!'
