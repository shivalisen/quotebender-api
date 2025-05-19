from flask import render_template, request, abort, jsonify
from app import app, db, pydantic_models, db_models
from sqlalchemy import select, func

def query_db(params: pydantic_models.Params) -> list[db_models.Quote]:
  filters = []
  if params.character is not None:
    filters.append(db_models.Quote.character == params.character)
  if params.season is not None:
    filters.append(db_models.Episode.season_number == params.season)
    if params.episode is not None:
      filters.append(db_models.Episode.number == params.episode)

  stmt = (
    select(db_models.Quote)
    .join(db_models.Quote.episode)
    .where(*filters)
    .order_by(
      db_models.Episode.season_number,
      db_models.Episode.number
    )
  )

  try:
    quotes = db.session.scalars(stmt).all()
    return quotes
  except:
    abort(500)

def query_db_random() -> db_models.Quote:
  stmt = select(db_models.Quote).order_by(func.random()).limit(1)

  try:
    quote = db.session.scalars(stmt).first()
    return quote
  except:
    abort(500)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/quotes')
def get_quotes():
  params = request.args.to_dict()
  try:
    validated_params = pydantic_models.Params(**params)

  except:
    abort(400)    

  res = query_db(validated_params)

  quotes = [{
    'quote': q.quote,
    'character': q.character,
    'episode_name': q.episode_name,
    'season_number': q.episode.season_number,
    'episode_number': q.episode.number
  } for q in res]

  return jsonify(quotes), 200
       

@app.route('/quotes/random')
def get_random_quotes():
  q = query_db_random()

  return jsonify({
    'quote': q.quote,
    'character': q.character,
    'episode_name': q.episode_name,
    'season_number': q.episode.season_number,
    'episode_number': q.episode.number
  }), 200