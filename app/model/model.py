import pickle
import pandas as pd
import subprocess
import os
from pathlib import Path
from sklearn.feature_selection import VarianceThreshold

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f'{BASE_DIR}/trained_model-{__version__}.pkl', 'rb') as f:
    model = pickle.load(f)

# Modelling helper
def desc_calc(input_data):
    # Reads in saved regression model
    # load_model = pickle.load(open('trained_model-0.1.0.pkl', 'rb'))
    
    # Remove low variance
    selection = VarianceThreshold(threshold=(.8 * (1 - .8)))    
    X_model = selection.fit_transform(input_data)

    # Apply model to make predictions
    prediction = model.predict(X_model)

    prediction_output = pd.Series(prediction, name='pIC50')
    molecule_name = pd.Series(input_data[1], name='molecule_name')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    
    return df