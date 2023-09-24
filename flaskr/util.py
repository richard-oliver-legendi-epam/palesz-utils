from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('util', __name__)

# werkzeug - szerszam

# Use single-quotes for string literals, e.g. 'my-identifier' , but use double-quotes for strings that are likely to contain single-quote characters as part of the string itself


@bp.route('/dilution', methods=('GET', 'POST'))
def dilution():
    if request.method == 'POST':
        try:
            volume: float = float(request.form['volume'])
            act_alcohol_level : float = float(request.form['act_alcohol_level'])
            target_alcohol_level : float= float(request.form['target_alcohol_level'])

            return render_template('util/dilution.html')
        except Exception as e:
            flash(str(e))
            return render_template('util/dilution.html')
    else:
        return render_template('util/dilution.html')
