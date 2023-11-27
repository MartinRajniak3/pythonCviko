#!/usr/bin/env python3
from flask import Flask, jsonify, request

MOVIES = list()
MOVIES.append({"title": "Star Wars: New Hope", "genre": "sci-fi"})

app = Flask(__name__)

@app.route("/api/")
def index():
    return "Ahoj z API"

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(MOVIES)

@app.route("/api/movies", methods=["POST"])
def add_movie():
    movie = request.json
    MOVIES.append(movie)
    return jsonify(movie), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

