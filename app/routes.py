from flask import render_template, request, abort, jsonify
from app import app, db, pydantic_models, db_models
from sqlalchemy import select

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/quotes')
def get_quotes():
    params = request.args.to_dict()
    try:
      val_params = pydantic_models.Params(**params)

    except:
      abort(400)    

@app.route('/quotes/random')
def get_random_quotes():
    params = request.args.to_dict()