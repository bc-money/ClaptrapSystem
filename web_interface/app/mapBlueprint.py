import functools
import sys
from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db

bp = Blueprint('map', __name__, url_prefix='/map')
# map/publish
@bp.route('/publish', methods=['POST'])
def publishPoint():
	req_data = request.form
	print req_data
	if req_data == None:
		return ("Didn't get the data")
	else:
		return("got it!")

