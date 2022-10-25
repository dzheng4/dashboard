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
from data_repo import california_df
import json
from urllib.request import urlopen
from apps import templates

layout = html.Div([
    templates.createMenu(),
    dbc.Row(
        dbc.Col(
            html.Table(
                [
                    html.Tr(
                        html.H3('California Vaccine Distribution Dashboard')
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
                    max_date_allowed = datetime(2022, 9, 28),
                    initial_visible_month = datetime(2021, 1, 18),
                    start_date = datetime(2020, 11, 29),
                    end_date = datetime(2022, 9, 28)
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
                    id = 'california_graph_1'
                )
            ]), width = 12
        )
    ),

 

    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Graph(
                    id = 'california_graph_2'
                )
            ]), width = 12
        )
    ),

    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Graph(
                    id = 'california_graph_3'
                )
            ]), width = 12
        )
    ),

    templates.backHome()


])

@app.callback(
    Output('california_graph_1','figure'),
    Output('california_graph_2','figure'),
    Output('california_graph_3','figure'),
    Input('submit', 'n_clicks'),
    State('my-date-picker-range', 'start_date'), 
    State('my-date-picker-range', 'end_date'),
)

def make_figures(n_clicks:int, Start_date: datetime, End_date: datetime):
    filtered_df = california_df.copy()
    filtered_df['date'] = pd.to_datetime(filtered_df['date'])
    filtered_df = filtered_df[(filtered_df['date'] >= Start_date) & (filtered_df['date'] <= End_date)]

    fig1 = px.line(
        filtered_df,
        x = 'date',
        y = ['doses_shipped', 'doses_delivered'],
        title = 'Daily Doses Shipped/Delivered'
    )

    fig1.update_layout(
        legend = dict(title = '')
    )
    

    fig2 = px.line(
        filtered_df,
        x = 'date',
        y = ['cumulative_doses_shipped', 'cumulative_doses_delivered'],
        title = 'Cumulative Doses Shipped/Delivered'
    )

    fig2.update_layout(
        legend = dict(title = '')
    )

    fig3 = px.line(
        filtered_df,
        x = 'date',
        y = 'cdc_pharmacy_doses_delivered',
        title = 'CDC Pharmacy Doses Delivered'
    )

    fig3.update_layout(
        legend = dict(title = '')
    )





    return fig1, fig2, fig3