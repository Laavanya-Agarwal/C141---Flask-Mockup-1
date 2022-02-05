from flask import Flask, jsonify, request
import csv

all_movies = []
with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:] #copies data from the 1st row to the last row (not 0th row) - moving into all_movies

liked_movies = []
disliked_movies = []
notwatched_movies = []

#GET REQUEST - gets details of movie
app = Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0], #shows first movie from list - one movie at a time
        "status": "Success!"
    })
if __name__ == "__main__":
    app.run()

#POST REQUEST - takes our input (if liked/disliked/notwatched)
#liked_movies
@app.route("/liked-movie", methods = ["POST"])
def liked_movie():
    movie = all_movies[0] #current movie
    all_movies = all_movies[1:] #the 0th row (now the 0th row starts from the original 1st row) gets removed
    liked_movies.append(movie) #moved to the liked_movies list
    return jsonify({
        "status": "Success!"
    }), 201 #if not working, it will show 201 error

#disliked_movies
@app.route("/disliked-movie", methods = ["POST"])
def disliked_movie():
    movie = all_movies[0] #current movie
    all_movies = all_movies[1:] #the 0th row (now the 0th row starts from the original 1st row) gets removed
    disliked_movies.append(movie) #moved to the disliked_movies list
    return jsonify({
        "status": "Success!"
    }), 201 #if not working, it will show 201 error

#notwatched_movies
@app.route("/notwatched-movie", methods = ["POST"])
def notwatched_movie():
    movie = all_movies[0] #current movie
    all_movies = all_movies[1:] #the 0th row (now the 0th row starts from the original 1st row) gets removed
    notwatched_movies.append(movie) #moved to the notwatched_movies list
    return jsonify({
        "status": "Success!"
    }), 201 #if not working, it will show 201 error