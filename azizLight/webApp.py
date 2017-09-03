#!/usr/bin/env python

from flask import Flask, jsonify, render_template

# Add blueprint 
from lightsAPI import limitless 

app = Flask(__name__)
# Register API
app.register_blueprint(limitless, url_prefix = "/lights")

@app.route("/")
def index():
    print(printRoutes())
    return render_template("index.html")

# Print all routes
# See: https://stackoverflow.com/a/17250154
def printRoutes():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__

    return jsonify(func_list)

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8888, debug=True)
    app.run(host="127.0.0.1", port=8888, debug=True)
