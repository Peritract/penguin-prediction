# Imports

import json
import pickle

import pandas as pd
import web

# Load the model
with open('./models/penguin_classifier', 'rb') as file:
    model = pickle.load(file)


# The predictor function

def predict_penguin(penguin):
    """Predicts a penguin's species based on dimensions."""

    # Create a dataframe matching the model's X order
    X = pd.DataFrame(columns=['culmen_length_mm',
                              'culmen_depth_mm',
                              'flipper_length_mm',
                              'body_mass_g'])

    # Add the penguin to the empty df    
    X = X.append(penguin, ignore_index=True)

    # Return a prediction
    return model.predict(X)[0]


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