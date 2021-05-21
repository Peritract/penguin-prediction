# Imports

import json

import web

from scripts.predict import predict_penguin

# Set up the URL routes

urls = (
    '/', 'Index',
    '/predict', 'Predict'
)

# Define how the app will respond to routes

class Index:
    def GET(self):
        return "This app provides penguin-prediction services."


class Predict:
    def POST(self):
        # Extract the JSON data from the request
        data = json.loads(web.data())

        # Make the prediction
        pred = predict_penguin(data)

        # Return the response
        return json.dumps({'prediction': pred})


if __name__ == "__main__":

    # Create an application with the routes set up
    app = web.application(urls, globals())

    # Run the app
    app.run()
