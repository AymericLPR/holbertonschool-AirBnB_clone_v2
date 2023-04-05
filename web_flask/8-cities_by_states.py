#!/usr/bin/python3
""" doc """
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def listStatesCities():
    # Get all the states objects
    States = storage.all(State)
    Cities = storage.all(City)

    return render_template("8-cities_by_states.html", states=States,
                           cities=Cities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
