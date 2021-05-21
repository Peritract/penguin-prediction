import pickle

import pandas as pd

# Load the model
with open('./models/penguin_classifier', 'rb') as file:
    model = pickle.load(file)

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