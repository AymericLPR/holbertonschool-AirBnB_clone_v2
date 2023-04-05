#!/usr/bin/python3
""" doc """
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def listAll():
    # Get all the states objects
    listOfStates = storage.all(State)
    return render_template("7-states_list.html", states=listOfStates)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
