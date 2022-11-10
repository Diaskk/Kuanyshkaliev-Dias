from flask import Blueprint, render_template, request, flash
from flask_login import login_required,current_user
from . import db
from .models import Food

custom = Blueprint('custom', __name__)

@custom.route('/custom', methods=['GET', 'POST'])
@login_required
def addRecipe():
    if request.method == 'POST':
        name = request.form.get('code_name')
        trueName = request.form.get('full_name')
        pic = request.form.get('cus_pic')
        description = request.form.get('recipe')

        if len(name) < 1:
            flash('Try again', category='error')
        elif len(trueName) < 1:
            flash('Try again', category='error')
        elif len(pic) < 1:
            flash('Try again', category='error')
        elif len(description) < 1:
            flash('Try again', category='error')
        else:
            new_rec = Food(name=name, trueName=trueName, pic=pic, description=description)
            db.session.add(new_rec)
            db.session.commit()
            flash('Recipe added', category='success')
    return render_template("custom.html", user=current_user)