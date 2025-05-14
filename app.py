from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
movies = pd.read_csv(r"C:\Users\varun\Desktop\movie_recommendation_site\movies.csv")

@app.route('/')
def index():
    query = request.args.get('query', '').lower()
    if query:
        results = movies[movies['title'].str.lower().str.contains(query)]
    else:
        results = movies.sample(10)
    return render_template('index.html', movies=results.to_dict(orient='records'))

@app.route('/movie/<title>')
def movie(title):
    movie_data = movies[movies['title'] == title].iloc[0]
    return render_template('movie.html', movie=movie_data)

if __name__ == '__main__':
    app.run(debug=True)
