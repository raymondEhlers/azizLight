#!/usr/bin/env python

import enum

from flask import Blueprint, render_template
from flask_restful import Resource, Api

limitless = Blueprint("limitlessInterface", __name__)
api = Api(limitless)

# TODO: Should probably be the hex value associated with the light
class Location(enum.Enum):
    door = 0
    livingRoom = 1

class State(enum.Enum):
    off = 0
    on = 1

class Lights(Resource):
    def get(self, lightLocation):
        # Query the status of the light
        print(lightLocation)
        lightLocation = Location[lightLocation]
        return lightLocation.name

    def put(self, lightLocation, state):
        # Set the request light to the request state
        state = State[state]

api.add_resource(Lights, "/<string:lightLocation>")
