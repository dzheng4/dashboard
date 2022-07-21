'''
 # @ Create Time: 2022-07-18 13:27:39.553419
'''

import pathlib
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True,
    meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0'}],
    external_stylesheets=[dbc.themes.LUX]
)

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

def load_data(data_file: str) -> pd.DataFrame:
    '''
    Load data from /data directory
    '''
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("data").resolve()
    return pd.read_csv(DATA_PATH.joinpath(data_file))

if __name__ == "__main__":
    app.run_server(debug=True)
