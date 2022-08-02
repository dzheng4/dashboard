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
from data_repo import newyork_df, fips_df
import json
from urllib.request import urlopen

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../states_data/NY").resolve()

layout = html.Div([
    # All elements from the top of the page
    dbc.Row([
        dbc.Col(
            html.Div(
                dcc.DatePickerRange(
                    id = 'my-date-picker-range',
                    min_date_allowed = datetime(2020, 12, 14),
                    max_date_allowed = datetime(2022, 7, 8),
                    initial_visible_month = datetime(2020, 12, 14),
                    start_date = datetime(2020, 12, 14),
                    end_date = datetime(2021, 1, 14)
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
                        html.Th('New York Vaccine Administration Dashboard')
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
                    id = 'ny_graph'
                )
            ]), width = 12
        )
    ),

])

@app.callback(
    Output('ny_graph','figure'),
    Input('submit', 'n_clicks'),
    State('my-date-picker-range', 'start_date'), 
    State('my-date-picker-range', 'end_date'),
)

def make_figures(n_clicks:int, Start_date: datetime, End_date: datetime):
    grouped_df = newyork_df
    grouped_df['Report as of'] = pd.to_datetime(grouped_df['Report as of'])
    grouped_df = grouped_df[(grouped_df['Report as of'] >= Start_date) & (grouped_df['Report as of'] <= End_date)]
    # grouped_df['Month'] = grouped_df['Report as of'].dt.to_period('M')
    grouped_df['Month'] = grouped_df['Report as of'].apply(lambda x: x.strftime('%Y-%m'))

    df = pd.DataFrame({'Doses':grouped_df.groupby(['County','Month'])['First Dose'].sum()}).reset_index()

    # path = "fips2county.tsv"
    # FipsDF = pd.read_csv(path, sep='\t', header='infer', dtype=str, encoding='latin-1')
    FipsDF = fips_df
    FipsDF = FipsDF[FipsDF['StateName']=='New York']
    CountyDf = FipsDF[['CountyName','CountyFIPS']]

    df = CountyDf.merge(df, how='inner', left_on='CountyName', right_on='County').drop_duplicates()
    df['CountyFIPS'] = df['CountyFIPS'].astype('string')

    print(df)

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
        animation_frame='Month'
    )

    fig1.update_layout(
        title_text='New York Summary',
        geo_scope='usa',
        margin={'r': 0, 't': 0, 'l': 0, 'b': 0}
    )

    fig1.update_geos(
        center=dict(lon=-73.94,lat=42.5),
        lataxis_range=[44,48],
        lonaxis_range=[280,300]
    )

    return fig1