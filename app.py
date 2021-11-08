"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request

from mbta_helper import find_stop_near, get_nearest_station, main


app = Flask(__name__)


@app.route('/index/', methods=["GET", "POST"])
def MBTA_STATION():
    if request.method == "POST":
        place_name = (request.form['location'])
        station = find_stop_near(place_name)
        
        if station:
            return render_template(
                'mbta_station.html',
            )
        else:
            return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True)
