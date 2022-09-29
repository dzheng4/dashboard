from datetime import datetime
from tokenize import group
from flask import g
import pandas as pd
import numpy as np
import json
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pathlib
from app import app
from data_repo import penn_retail_df, fips_df
import json
from urllib.request import urlopen
import requests
import csv
from apps import templates

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../states_data/PA").resolve()

layout = html.Div([
    templates.createMenu(),
    # All elements from the top of the page
    dbc.Row([
        dbc.Col(
            html.Div(
                dcc.DatePickerRange(
                    id = 'my-date-picker-range',
                    min_date_allowed = datetime(2021, 1, 18),
                    max_date_allowed = datetime(2022, 9, 28),
                    initial_visible_month = datetime(2021, 1, 18),
                    start_date = datetime(2021, 1, 18),
                    end_date = datetime(2022, 9, 28)
                ),
            ), width = 6
        ),

        ## Button element
        dbc.Col(
            html.Div(
                dbc.Button(
                    'Submit',
                    id = 'submit',
                    style = {
                        'background-color' : '#F56262'    
                    }
                )
            ), width = 3
        ),
    ], className = "g-0"), #className = "g-0" sets the column gutter size to 0. This removes column padding.

    dbc.Row(
        dbc.Col(
            html.Table(
                [
                    html.Tr(
                        html.Th('Pennsylvania Vaccine Distribution Dashboard')
                    )
                ],
                style = {
                    'margin-left': '50px',
                    'margin-top': '20px',
                    'margin-bottom': '20px',
                    'width': '70%',
                    'border': '2px solid black',
                    'text-align': 'center',
                    'font-family': 'Century Gothic'
                }
            )
        )
    ),
    
    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Graph(
                    id = 'penn_map_graph'
                )
            ]), width = 12
        )
    ),


    templates.backHome()


])

@app.callback(
    Output('penn_map_graph','figure'),
    Input('submit', 'n_clicks'),
    State('my-date-picker-range', 'start_date'), 
    State('my-date-picker-range', 'end_date'),
)

def make_figures(n_clicks:int, Start_date: datetime, End_date: datetime):
    penn_df = penn_retail_df
    grouped_penn_df = penn_df
    grouped_penn_df['Date'] = pd.to_datetime(grouped_penn_df['Date'])
    grouped_penn_df = grouped_penn_df[(grouped_penn_df['Date'] >= Start_date) & (grouped_penn_df['Date'] <= End_date)]


    location = grouped_penn_df['Georeferenced Latitude & Longitude'].str.split(' ', expand=True)
    location.rename(columns={0:'col_1', 1:'col_2', 2:'col_3'}, inplace=True)

    location['col_2'] = location['col_2'].str.slice(start=1)
    location['col_3'] = location['col_3'].str.slice(stop=-1)
    grouped_penn_df['lon'] = location['col_2'].astype(float)
    grouped_penn_df['lat'] = location['col_3'].astype(float)
    grouped_penn_df.dropna(inplace=True)

    print(grouped_penn_df)


    fig = px.scatter_mapbox(
        grouped_penn_df,
        lon = grouped_penn_df['lon'],
        lat = grouped_penn_df['lat'],
        zoom = 7,
        color = grouped_penn_df['Doses'],
        size = grouped_penn_df['Doses'],
        width = 1800,
        height = 900,
        title = 'Penn Map Graph'
    )

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":20,"t":50,"l":0,"b":10})


    return fig