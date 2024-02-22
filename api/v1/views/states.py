#!/usr/bin/python3
from models.state import State
from flask import Flask, jsonify,Blueprint , request, abort
from api.v1.views import app_views
from api.v1.app import error_404


@app_views.route("/states/<state_id>", methods=["GET"])
def states(state_id):
    state = State.get(state_id)
    if not state:
        # abort (404)
        return error_404()
