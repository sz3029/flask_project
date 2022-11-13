from flask import render_template, request, Blueprint
# index page
bp = Blueprint('core', __name__)
@bp.route('/')
def index():
    return render_template('index.html')

