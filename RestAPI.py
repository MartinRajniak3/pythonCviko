#!/usr/bin/env python3
from flask import Flask, jsonify, request

MOVIES = list()
MOVIES.append({"id": 0, "title": "Star Wars: New Hope", "genre": "sci-fi"})
My_next_id = 1

app = Flask(__name__)

@app.route("/api/")
def index():
    return "Ahoj z API"

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(MOVIES)

@app.route("/api/movies", methods=["POST"])
def add_movie():
    global My_next_id
    movie = request.json
    movie["id"] = My_next_id
    My_next_id += 1
    MOVIES.append(movie)
    return jsonify(movie), 201

@app.route("/api/movies/<id>", methods=["DELETE"])
def del_movie(id):
    for movie in MOVIES:
        if movie["id"] == int(id):
             temp = movie
             MOVIES.remove(movie)
             return jsonify(movie), 200
        return jsonify({"error": "id not found"}), 404

@app.route("/api/movies/<id>", methods=["PUT"])
def edit_movie(id):
    movie_edit = request.json
    for movie in MOVIES:
        if movie["id"] == int(id):
             if "title" in movie_edit.keys():
                 movie["title"] = movie_edit["title"]
             if "genre" in movie_edit.keys():
                 movie["genre"] = movie_edit["genre"]

             return jsonify(temp), 200
        return jsonify({"error": "id not found"}), 404



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

