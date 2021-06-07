# Imports

import json

import web
from web import form

from scripts.predict import predict_penguin

# Set up the URL routes

urls = (
    '/', 'Index',
    '/predict', 'Predict',
    '/predict_form', 'PredictForm'
)

# Use HTML templates

render = web.template.render('templates') # your templates

# Create a form
predict_form = form.Form(form.Textbox("culmen_length_mm",
                                      description="Culmen length (mm)"),
                         form.Textbox("culmen_depth_mm",
                                      description="Culmen depth (mm)"),
                         form.Textbox("flipper_length_mm",
                                      description="Flipper length (mm)"),
                         form.Textbox("body_mass_g",
                                      description="Body mass (g)"),
                         form.Button("submit", type="submit",
                                     description="Predict")
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

class PredictForm:
    def GET(self):
        f = predict_form()
        return render.predict_form(f)

    def POST(self):
        # Extract the data
        data = web.input()

        # Convert all the values to numbers
        safe_data = {}
        for k, v in data.items():
            if v != '':
                safe_data[k] = float(v)

        # Make the prediction
        pred = predict_penguin(safe_data)

        # Fill & return the prediction template
        return render.prediction(safe_data['culmen_length_mm'],
                                 safe_data['culmen_depth_mm'],
                                 safe_data['flipper_length_mm'],
                                 safe_data['body_mass_g'],
                                 pred)

if __name__ == "__main__":

    # Create an application with the routes set up
    app = web.application(urls, globals())

    # Run the app
    app.run()
