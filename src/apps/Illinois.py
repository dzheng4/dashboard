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
from data_repo import illinois_df, fips_df
import json
from urllib.request import urlopen
from apps import templates

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../states_data/IL").resolve()

layout = html.Div([
    dcc.Location(
        id = 'url-illinois',
        refresh = True
    ),

    dbc.Row(
        templates.createMenu()
    ),

    dbc.Row(
        dbc.Col(
            html.Table(
                [
                    html.Tr(
                        html.Th('Illinois Cumulative Vaccinated Dashboard')
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
                    id = 'illinois_graph'
                )
            ]), width = 12
        )
    ),

    templates.backHome()

])

@app.callback(
    Output('illinois_graph','figure'),
    Input('url-illinois', 'pathname')
)

def make_figures(pathname):
    grouped_illinois_df = illinois_df

    FipsDF = fips_df
    FipsDF = FipsDF[FipsDF['StateName']=='Illinois']
    CountyDf = FipsDF[['CountyName','CountyFIPS']]

    df = CountyDf.merge(grouped_illinois_df, how='inner', left_on='CountyName', right_on='County').drop_duplicates()
    df['CountyFIPS'] = df['CountyFIPS'].astype('string')

    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    df['Fully Vaccinated Percentage'] = df['% Population Fully Vaccinated'].str.split('%', expand=True)[0]

    df['Fully Vaccinated Percentage'] = df['Fully Vaccinated Percentage'].astype(float)
    
    fig3 = px.choropleth(
        df,
        geojson=counties,
        locations=('CountyFIPS'),
        color='Fully Vaccinated Percentage',
        title='County Doses',
        color_continuous_scale=px.colors.sequential.Blues,
        hover_name=('County'),
        scope='usa',
    )

    fig3.update_layout(
        title_text='Penn Summary',
        geo_scope='usa',
        margin={'r': 0, 't': 0, 'l': 0, 'b': 0}
    )

    fig3.update_geos(
        center=dict(lon=-89,lat=40),
        lataxis_range=[39.5,42.5],
        lonaxis_range=[270,300]
    )


    return fig3