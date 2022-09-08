from datetime import datetime
import pandas as pd
import numpy as np
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pathlib
from app import app
from data_repo import connecticut_df
from urllib.request import urlopen
from apps import templates

layout = html.Div([
    templates.createMenu(),
    dbc.Row(
        dbc.Col(
            html.Table(
                [
                    html.Tr(
                        html.H3('Connecticut Vaccine Distribution Dashboard')
                    )
                ],
                style = {
                    'margin-left': '280px',
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
    # All elements from the top of the page
    dbc.Row([
        dbc.Col(
            html.Div(
                dcc.DatePickerRange(
                    id = 'my-date-picker-range',
                    min_date_allowed = datetime(2020, 11, 29),
                    max_date_allowed = datetime(2022, 7, 31),
                    initial_visible_month = datetime(2021, 1, 18),
                    start_date = datetime(2020, 11, 29),
                    end_date = datetime(2022, 7, 31)
                ),
            ), width = 2,
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
            html.Div([
                dcc.Graph(
                    id = 'conn_graph_1'
                )
            ]), width = 12
        )
    ),

    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Graph(
                    id = 'conn_graph_2'
                )
            ]), width = 12
        )
    ),


    templates.backHome()


])

@app.callback(
    Output('conn_graph_1','figure'),
    Output('conn_graph_2','figure'),
    Input('submit', 'n_clicks'),
    State('my-date-picker-range', 'start_date'), 
    State('my-date-picker-range', 'end_date'),
)

def make_figures(n_clicks:int, Start_date: datetime, End_date: datetime):
    filtered_df = connecticut_df
    filtered_df['Reporting period end date'] = pd.to_datetime(filtered_df['Reporting period end date'])
    filtered_df = filtered_df[(filtered_df['Reporting period end date'] >= Start_date) & (filtered_df['Reporting period end date'] <= End_date)]
    fig1 = px.line(filtered_df, x = 'Reporting period end date', y = 'Cumulative')

    fig2 = px.line(filtered_df, x = 'Reporting period end date', y = 'Weekly total')

    return fig1, fig2