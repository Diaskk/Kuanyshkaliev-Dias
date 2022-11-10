import requests as requests
from flask import Blueprint, make_response, render_template, request, flash
from flask_login import current_user

from .models import Food

recipe = Blueprint('recipe', __name__)


@recipe.route('/search', methods=['GET'])
def search():
    global payload
    args = request.args['name']

    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={args}"
    headers = {
        "accept": "application/json"
    }
    food = Food()
    dbExist = food.checkInDb(args)

    if dbExist:
        payload = dbExist
        return make_response(render_template('result.html', payload=payload, user=current_user))
    else:
        try:
            response = requests.get(url, headers=headers)
            response2 = response.json()

            payload = {
                "name": args,
                "trueName": response2["meals"][0]["strMeal"],
                "description": response2["meals"][0]["strInstructions"],
                "pic": response2["meals"][0]["strMealThumb"],

            }

            recipe1 = Food(**payload)

            recipe1.addToDb()
        except KeyError or TypeError or NameError:
            flash('Not Found', category='error')

        return make_response(render_template('result.html', payload=payload, user=current_user))
