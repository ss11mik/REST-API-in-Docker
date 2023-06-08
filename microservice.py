# Python-based microservice
#
# implements REST API using Flask and SQLite
#
# author: Ondrej Mikula
# 2023


from flask import Flask, jsonify, request, g
from gevent.pywsgi import WSGIServer
import pysqlite3 as sqlite3



app = Flask(__name__)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect("movies.db")

    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def exec_query(query, params=""):
    db = get_db()
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    db.commit()
    return [dict(x) for x in result], cursor.rowcount




@app.route('/movies', methods = ['GET'])
def movies_list():
    query, _ = exec_query("SELECT * FROM movies;")
    return jsonify(query)


@app.route('/movies/<int:id>', methods = ['GET'])
def movie_detail(id):
    try:
        query, _ = exec_query(f"SELECT * FROM movies WHERE id=?;", [id])
    except sqlite3.IntegrityError:
        return "Bad Request.\n", 400

    if len(query) < 1:
        return f"{id} not found.\n", 404

    return jsonify(query[0])


@app.route('/movies', methods = ['POST'])
def create_movie():
    movie_dict = request.json

    if movie_dict.get('title') == None or movie_dict.get('release_year') == None:
        return "Bad Request.\n", 400

    if movie_dict.get('description') == None:
        movie_dict['description'] = ""

    try:
        query, _ = exec_query(f""" INSERT INTO movies (title, description, release_year) VALUES (?, ?, ?) RETURNING id, title, description, release_year;""",
                                [
                                    movie_dict['title'],
                                    movie_dict['description'],
                                    movie_dict['release_year']
                                ])
    except sqlite3.IntegrityError:
        return "Bad Request.\n", 400

    return jsonify(query)


@app.route('/movies/<int:id>', methods = ['PUT'])
def update_movie(id):
    movie_dict = request.json

    allowed_params = ["title", "description", "release_year"]
    keys = movie_dict.keys() & allowed_params
    movie_dict = {k: movie_dict[k] for k in keys}

    if len(movie_dict) < 1:
        return "Bad Request.\n", 400


    q = f"UPDATE movies SET " + ', '.join(
        "{}=?".format(k) for k in movie_dict.keys()) + f" WHERE id=? RETURNING id, title, description, release_year;"

    try:
        query, num = exec_query(q, list(movie_dict.values()) + [id])
    except sqlite3.IntegrityError:
        return "Bad Request.\n", 400

    if len(query) < 1:
        return f"{id} not found.\n", 404

    movie_dict['id'] = id
    return jsonify(movie_dict)




if __name__ == '__main__':
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()
