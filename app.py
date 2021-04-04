from flask import Flask, render_template, abort

from data.tours import tours, page

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def render_main():
    return render_template('index.html', tours=tours, page=page)


@app.route('/departures/<departure>/')
def render_products(departure):
    return render_template('departure.html', page=page, departure=departure,
                           tours=list(filter(lambda x: x["departure"] == departure, tours.values())))


@app.route('/tours/<int:tour_id>/')
def render_about(tour_id):
    try:
        return render_template('tour.html', tour=tours[tour_id], page=page)
    except KeyError:
        abort(404)


app.run(port=5021, debug=True)
