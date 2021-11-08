"""
Simple "Hello, World" application using Flask
"""

from logging import error
from flask import Flask, render_template, request
from flask.scaffold import _matching_loader_thinks_module_is_package
from mbta_helper import find_stop_near, get_nearest_station, main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location/', methods=['GET','POST'])
def MBTA_STATION():
    if request.method == "POST":
        place_name = (request.form['location'])
        station = find_stop_near(place_name)
        
        if station:
            return render_template('mbta_station.html')
        else:
            return render_template('mbta_station.html', error=True)
    return render_template('mbta_station.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)
