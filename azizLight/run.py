#!/usr/bin/env python

import logging
import pprint
import ruamel.yaml as yaml

# Config
with open("config.yaml", "rb") as f:
    parameters = yaml.load(f, Loader=yaml.SafeLoader)
print("parameters: {0}".format(pprint.pformat(parameters)))

# By not setting a name, we get everything!
logger = logging.getLogger("")

# Setup logger
utilities.setupLogging(logger, parameters["loggingLevel"], receiverParameters["debug"], "webApp")

# Imports are below here so that they can be logged
from webApp import app

def runDevelopment():
    logger.info("Starting Aziz, Light app")
    # Turn on flask debugging
    app.debug = parameters["debug"]
    # Careful with threaded, but it can be useful to test the status page, since the post request succeeds!
    app.run(host=parameters["receiverIP"],
            port=parameters["receiverPort"])#, threaded=True)

if __name__ == "__main__":
    runDevelopment()
