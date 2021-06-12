# Penguin Prediction

This repository contains code to do the following:

1. Train a model to predict penguin species based on penguin dimensions.
2. Offer the above model's predictions as an API.

The purpose of this repository is to act as a teaching tool, providing both an example of the finished product (on the `main` branch) and a simple scaffold to start building from (`partial-penguin-prediction`).

The completed app does not contain code for dealing with malformed requests; this is left as an exercise for the reader.

## Installation

`pip install -r requirements.txt`

## Running

`python app.py`

## Deployment

The API is currently deployed on Heroku; the files in this repository are those required for it to run in that environment specifically.

## Routes

The root URL is `https://penguin-predictions-api.herokuapp.com/`.

The following endpoints are available:

- [/](https://penguin-predictions-api.herokuapp.com/) - the root address, which responds to `GET` requests with a short description of the API.
- [/predict](https://penguin-predictions-api.herokuapp.com/predict) - the prediction endpoint, which responds to `POST` requests with a prediction of penguin species. 

When sending `POST` requests to the API endpoint, include the following four numeric fields in a JSON object:

- `culmen_length_mm`
- `culmen_depth_mm`
- `flipper_length_mm`
- `body_mass_g`

The response will be a JSON object with only one key, `prediction`, containing the species prediction as a string.

## Interface

Penguin prediction is also accessible through a UI at [/predict_form](https://penguin-predictions-api.herokuapp.com/predict).

## Data source

The data used in this project is sourced from the [Palmer Penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) dataset.