from datetime import datetime
import pandas as pd
import numpy as np
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pathlib
from app import app
from urllib.request import urlopen
from apps import templates




layout = html.Div([

    dbc.Row([
        templates.navbar()
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col(
            html.Iframe(
                src="https://public.tableau.com/views/Parquet_Dashboard/VaccineAdministrationSummary?:language=en-US&:display_count=n&:origin=viz_share_link?:language=en-US&:display_count=n&:origin=viz_share_link?:showVizHome=no&:embed=true",
                style={"height": "1200px", "width": "1200px"}
            ), width={"size": 6, "offset": 3}
        )
    ]),

    
    templates.backHome()


])

