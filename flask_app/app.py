from flask import Flask, request, jsonify
import DB
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
   df = DB.getMovie()
   name = "movie name: " + df.loc[0, 'Name']
   return name

@app.route('/api/get_movie_name')
def get_movie_name():
   movie_name = request.args.get('name')
   DB.getMovie(DB.create_connection)
   

if __name__ == '__main__':
   app.run()