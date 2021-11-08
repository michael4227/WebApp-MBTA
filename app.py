"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request

from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/index/', methods=["GET", "POST"])
def MBTA_STATION():
    if request.method == "POST":
        place_name = (request.form['location'])
        dic_st_wl = find_stop_near(place_name)
        
        if dic_st_wl:
            return render_template(
                'mbta_station.html',
                nearest_station = dic_st_wl[0],
                wheelchair = dic_st_wl[1]
            )
        else:
            return render_template("error.html")
    return render_template('index.html', error=None)


if __name__ == '__main__':
    app.run(debug=True)
