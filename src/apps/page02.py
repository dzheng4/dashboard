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

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../states_data/PA").resolve()

layout = html.Div([
    dcc.Location(
        id = 'url-page2',
        refresh = True
    ),
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
                    id = 'penn_graph2'
                )
            ]), width = 12
        )
    ),

])

@app.callback(
    Output('penn_graph2','figure'),
    Input('url-page2', 'pathname')
)

def make_figures(pathname):
    penn_df = penn_retail_df
    grouped_penn_df = penn_df
    grouped_penn_df['Date'] = pd.to_datetime(grouped_penn_df['Date'])
    grouped_penn_df['Month'] = grouped_penn_df['Date'].dt.to_period('M')
    # print(grouped_penn_df)

    df = pd.DataFrame({'Doses':grouped_penn_df.groupby(by=['State','Month'])['Doses'].sum()}).reset_index()



    # path = "fips2county.tsv"
    # FipsDF = pd.read_csv(path, sep='\t', header='infer', dtype=str, encoding='latin-1')
    FipsDF = fips_df
    FipsDF = FipsDF[FipsDF['StateName']=='Pennsylvania']
    CountyDf = FipsDF[['CountyName','CountyFIPS']]

    # df = CountyDf.merge(df, how='inner', left_on='CountyName', right_on='County').drop_duplicates()
    # df['CountyFIPS'] = df['CountyFIPS'].astype('string')

    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
    # print(df)
    fig1 = px.choropleth(
        df,
        # geojson=counties,
        locations='State',
        color=('Doses'),
        title='County Doses',
        locationmode='USA-states',
        color_continuous_scale=px.colors.sequential.Plasma,
        # hover_name=('County'),
        scope='usa',
        animation_frame='Month'
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



    return fig1