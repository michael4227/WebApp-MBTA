"""
Simple "Hello, World" application using Flask
"""

from logging import error
from flask import Flask, render_template, request
from flask.scaffold import _matching_loader_thinks_module_is_package
from mbta_helper import find_stop_near, get_nearest_station, main

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def MBTA_STATION():
    if request.method == "POST":
        place_name = (request.form['location'])
        try:
            station = find_stop_near(place_name)
            return render_template('mbta_station.html',
            location = place_name,
            output = station)
        except:
            return render_template('error.html',error=True)
    return render_template('index.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)