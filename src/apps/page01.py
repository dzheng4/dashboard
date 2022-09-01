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
                    max_date_allowed = datetime(2022, 6, 21),
                    initial_visible_month = datetime(2021, 1, 18),
                    start_date = datetime(2021, 1, 18),
                    end_date = datetime(2022, 6, 21)
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
                    id = 'penn_graph'
                )
            ]), width = 12
        )
    ),

    dbc.Row([
        dcc.RangeSlider(0,30,1, value=[5,15], id='slider'),
        html.Div(id='slider-output')
    ]),

    templates.backHome()

])

@app.callback(
    Output('penn_graph','figure'),
    Output('slider-output','children'),
    Input('submit', 'n_clicks'),
    State('my-date-picker-range', 'start_date'), 
    State('my-date-picker-range', 'end_date'),
    Input('slider', 'value')
)

def make_figures(n_clicks:int, Start_date: datetime, End_date: datetime, value:int):
    penn_df = penn_retail_df
    grouped_penn_df = penn_df
    grouped_penn_df['Date'] = pd.to_datetime(grouped_penn_df['Date'])
    grouped_penn_df = grouped_penn_df[(grouped_penn_df['Date'] >= Start_date) & (grouped_penn_df['Date'] <= End_date)]

    df = pd.DataFrame({'Doses':grouped_penn_df.groupby('County')['Doses'].sum()}).reset_index()

    # path = "fips2county.tsv"
    # FipsDF = pd.read_csv(path, sep='\t', header='infer', dtype=str, encoding='latin-1')
    FipsDF = fips_df
    FipsDF = FipsDF[FipsDF['StateName']=='Pennsylvania']
    CountyDf = FipsDF[['CountyName','CountyFIPS']]

    df = CountyDf.merge(df, how='inner', left_on='CountyName', right_on='County').drop_duplicates()
    df['CountyFIPS'] = df['CountyFIPS'].astype('string')

    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
    
    fig1 = px.choropleth(
        df,
        geojson=counties,
        locations=('CountyFIPS'),
        color=('Doses'),
        title='County Doses',
        color_continuous_scale=px.colors.sequential.Plasma,
        hover_name=('County'),
        scope='usa',
    )

    fig1.update_layout(
        title_text='Penn Summary',
        geo_scope='usa',
        margin={'r': 0, 't': 0, 'l': 0, 'b': 0}
    )

    fig1.update_geos(
        center=dict(lon=-78,lat=41),
        lataxis_range=[39.5,42.5],
        lonaxis_range=[280,300]
    )

    message = 'You have selected {}'.format(value)



    return fig1, message