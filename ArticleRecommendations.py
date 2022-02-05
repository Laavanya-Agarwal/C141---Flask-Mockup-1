from flask import Flask, jsonify, request
import csv

all_articles = []
with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:] #copies data from the 1st row to the last row (not 0th row) - moving into all_articles

liked_articles = []
disliked_articles = []

#GET REQUEST - gets details of article
app = Flask(__name__)
@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0], #shows first article from list - one article at a time
        "status": "Success!"
    })
if __name__ == "__main__":
    app.run()

#POST REQUEST - takes our input (if liked/disliked)
#liked_articles
@app.route("/liked-article", methods = ["POST"])
def liked_article():
    article = all_articles[0] #current article
    all_articles = all_articles[1:] #the 0th row (now the 0th row starts from the original 1st row) gets removed
    liked_articles.append(article) #moved to the liked_articles list
    return jsonify({
        "status": "Success!"
    }), 201 #if not working, it will show 201 error

#disliked_articles
@app.route("/disliked-article", methods = ["POST"])
def disliked_article():
    article = all_articles[0] #current article
    all_articles = all_articles[1:] #the 0th row (now the 0th row starts from the original 1st row) gets removed
    disliked_articles.append(article) #moved to the disliked_articles list
    return jsonify({
        "status": "Success!"
    }), 201 #if not working, it will show 201 error